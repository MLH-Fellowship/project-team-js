import unittest
import os
from flask import json
from playhouse.shortcuts import model_to_dict
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Javier Solis</title>" in html
        assert "<div id=\"user-picture\" class=\"user-picture\">" in html
        assert "<div class=\"main-content\">" in html

    def test_timeline(self):
        response_before = self.client.get('/api/timeline_post')
        assert response_before.status_code == 200
        assert response_before.is_json
        json_before = response_before.get_json()
        assert "timeline_posts" in json_before
        assert len(json_before['timeline_posts']) == 0
        # Create 2 posts
        post_1 = self.client.post(
            '/api/timeline_post',
            data={
                'name': 'John Doe',
                'email': 'john@example.com',
                'content': "Hello world, I'm John!"
            },
        )
        assert post_1.get_json()['id'] == 1
        post_2 = self.client.post(
            '/api/timeline_post',
            data={
                'name': 'Jane Doe',
                'email': 'jane@example.com',
                'content': "Hello world, I'm Jane!"
            },
        )
        assert post_2.get_json()['id'] == 2
        # Get posts
        response_after = self.client.get('/api/timeline_post')
        assert response_after.status_code == 200
        assert response_after.is_json
        json_after = response_after.get_json()
        assert "timeline_posts" in json_after
        assert len(json_after['timeline_posts']) == 2
        assert json_after['timeline_posts'][0]['name'] == 'Jane Doe'
        # TODO: Add more tests relating to the timeline page