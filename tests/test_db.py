import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# In-memory SQLite database for tests
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to database non-recursively because there is a
        # complete list of all models
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not necessary for in-memory databases but a good practice
        test_db.drop_tables(MODELS)

        test_db.close()

    def test_timeline_post(self):
        # Create 2 posts
        first_post = TimelinePost.create(
            name='John Doe',
            email='john@example.com',
            content="Hello word, I'm John!"
        )
        assert first_post.id == 1
        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content="Hello word, I'm Jane!"
        )
        assert second_post.id == 2
        # TODO: Get timeline posts and assert they are correct