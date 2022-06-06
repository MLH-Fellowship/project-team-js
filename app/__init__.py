import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


intro_blurb="""
Hi! My name is Javier Solis and I'm a junior at MIT learning computer science.
Some of my interests include Nintendo gaming, all-things GNU/Linux, writing, and exploring.
Feel free to look around by using the sidebar to peak into specific sections. 
"""

about_blurb = """
<p>(about me)</p>
"""

hobbies = [
    {'name':'Nintendo Video Games',
    'tags': ["Entertainment"],
    'description': "I enjoy playing Nintendo Video Games.",
    'picture_urls': [""]
    }
]

work_xp = [
    {'name': 'Undergraduate Research on Networking',
    'tags': ["Entertainment"],
    'start_date': "February, 2021",
    'end_date': "Present",
    'description': "In this research position at the Networks and Mobile Systems group (NMS) at the MIT Computer Science & Artificial Intelligence Laboratory (CSAIL) , I ...",
    'picture_urls': [""]
    }
]

adventures = [
]

user={
    "name": "Javier Solis",
    "pfp_url": "./static/img/logo.jpg", #pfp stands for "profile picture" 
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