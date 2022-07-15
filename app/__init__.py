from dataclasses import dataclass
from email.policy import default
import json
import os
from typing import Text
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import * 
from datetime import datetime
from pymysql import Time
from playhouse.shortcuts import model_to_dict
import re

load_dotenv()
app = Flask(__name__)

EMAIL_REGEX = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    my_db = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    my_db = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            host=os.getenv("MYSQL_HOST"),
            port=3306)

print(my_db)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = my_db

my_db.connect()
my_db.create_tables([TimelinePost])


# References to all the data
locations = json.load(open("./app/static/data/locations.json"))
intro_blurb= json.load(open("./app/static/data/intro_blurb.json"))["intro_blurb"]
about_blurb = json.load(open("./app/static/data/about_blurb.json"))["about_blurb"]
hobbies = json.load(open("./app/static/data/hobbies.json"))["hobbies"]
work_xp = json.load(open("./app/static/data/work_xp.json"))["work_xp"]

adventures = [
]

user={
    "name": "Javier Solis",
    "pfp_url": "https://drive.google.com/uc?export=view&id=1QyUK0PH-O1QKsDtw2tMDmtn3WRBrAeGw", #pfp stands for "profile picture" 
    "intro_blurb": intro_blurb,
    "about_blurb": about_blurb,
    "hobbies": hobbies,
    "work_xp": work_xp,
    "adventures": adventures, # TODO: Implement this feature in this file, instead of in locations.hs
}

@app.route('/')
def index():
    return render_template('index.html', username=user["name"], pfp_url=user["pfp_url"], intro=user["intro_blurb"], url=os.getenv("URL"))

@app.route('/about')
def about_page():
    return render_template('about.html', username=user["name"], pfp_url=user["pfp_url"], about_blurb=user["about_blurb"])

@app.route('/hobbies')
def hobby_page():
    return render_template('hobbies.html', username=user["name"], pfp_url=user["pfp_url"], hobbies_info=user["hobbies"])

@app.route('/work-xp')
def work_xp_page():
    return render_template('work_xp.html', username=user["name"], pfp_url=user["pfp_url"], work_xp_info=user["work_xp"])

@app.route('/adventures')
def adventures_page():
    return render_template('adventures.html', username=user["name"], pfp_url=user["pfp_url"])

@app.route('/adventures/locations', methods=['GET'])
def get_adventures_locations():
    return locations


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.values.get('name')
    email = request.values.get('email')
    content = request.values.get('content')
    
    if name == None or name == str():
        return "Invalid name", 400
    if content == None or content == str():
        return "Invalid content", 400
    if not re.match(EMAIL_REGEX, email):
        return "Invalid email", 400
    
    timeline_post = TimelinePost.create(name=name, email=email, content = content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {'timeline_posts': [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())]}

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    id = request.form['id']
    my_db.execute(TimelinePost.delete().where(TimelinePost.id == id))
    return {'id': id}

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', username=user["name"], pfp_url=user["pfp_url"], title="Timeline")