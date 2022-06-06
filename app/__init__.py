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
<h2>Personal Background</h2>
<p>
I grew up in a suburb town on the outskirts of Chicago, IL, known as <a href="https://en.wikipedia.org/wiki/Cicero,_Illinois">Cicero</a>. My parents are <a href="https://en.wikipedia.org/wiki/Blue-collar_worker">blue-collar workers</a> and come from a poor socioeconomic background.
Now in college, I primarily live in the greater Boston area.
</p>

<p>
Outside work, I enjoy playing Nintendo video games, learning the piano, learning more about GNU/Linux, and visiting new places, which you can read more about in my hobbies page.
I am also huge a supporter of the Free/Libre Software movement, and use open source software whenever possible.
</p>


<h2>Education</h2>
<p>
I am a rising Junior majoring in Computer Science at MIT. My main interests lie in system software & operating system engineering but I'm continuously exploring.
Through my journey at MIT, I've expanded my programming knowledge through an algorithmic and structural lens. I've also learned the programming languages of Python, TypeScript, C, and webdev.
At MIT I've also been a part of a few research groups, as detailed in the work experience page.
</p>

<h2>Contact</h2>
<p>
The most reliable way to reach me is via e-mail, at <code>javsolis@mit.edu</code>.
</p>
</p>
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
    'tags': ["research"],
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