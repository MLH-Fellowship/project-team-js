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
    {'name':'Gaming',
    'tags': ["entertainment"],
    'description': "I enjoy playing video games, and primarily those made by Nintendo and indie developers. When I was younger, I spent hours a day playing titles like The Legend of Zelda: Breath of the Wild, Splatoon 2, and Super Mario Odyssey. These days there's less time for long gaming sessions and I've come to play more shorter multiplayer games from series like Mario Kart and Mario Party. I also used to play a lot of Kerbal Space Program, a game where you can make your own rockets and visit planets.",
    'picture_urls': [""]
    },
    {'name':'Praticing the Piano',
    'tags': ["entertainment"],
    'description': "I've recently gotten into practicing the piano, with MIT having so many. I've primarily been learning video game songs such as Megalovania (from Undertale) and Lost Woods (from the Zelda series)",
    'picture_urls': [""]
    },
    {'name':'Listening to Podcasts',
    'tags': ["recreational", "informative"],
    'description': "I've also recently gotten into listening to podcasts from various people/groups and getting to learn new persperctives.",
    'picture_urls': [""]
    },
    {'name':'Learning More GNU/Linux',
    'tags': ["educational"],
    'description': "Since last year, I've become interested in learning all there is to know about GNU/Linux. To that avail, I often some of my free time learning new terminal commands & Linux components and trying out new Linux distros and versions.",
    'picture_urls': [""]
    },
    {'name':'Exploring',
    'tags': ["recreational"],
    'description': "I enjoy exploring new places. I picked this up upon arriving to MIT, where the greater Boston area has lots to discover. I enjoy biking while traveling, when possible.",
    'picture_urls': [""]
    }
]

work_xp = [
    {'name': 'Interconnected Embedded Systems Lab Assistant',
    'roles': ["Assistant"],
    'start_date': "February, 2022",
    'end_date': "May, 2022",
    'description': "Answering student questions throughout in-class lab, and carrying out 'checkoffs' with students, holding discussions that verify that they understand lab material. Serving a classroom with over 90 students, for 5 hours a week.",
    'picture_urls': [""]
    },
    {'name': 'Passive Measurement of Video Conferencing Quality',
    'roles': ["Researcher"],
    'start_date': "February, 2022",
    'end_date': "Present",
    'description': "Investigating the impact that different network factors have on video calling quality, like intermittent packet loss & lower bandwidth. Enhancing my research group's existing measurement software by developing processes that can parse network-level video ",
    'picture_urls': [""]
    },
    {'name': 'Engineering Design Workshop',
    'roles': ["Mentor"],
    'start_date': "June, 2021",
    'end_date': "August, 2021",
    'description': "Lead mentor and coordinator for 4 innovative high school engineering workshops held in Houston, San Francisco, Miami, and New Orleans. Each month-long workshop had 6-12 participants who worked in small teams on self-selected projects. The innovation was that 7 newly admitted MIT first-year students ran these programs in their respective high schools, with remote support from MIT.",
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