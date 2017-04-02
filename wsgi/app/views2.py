from app import app
from flask import render_template, request
import unirest
from forms import MessageForm
from app import database
from app import simple
from flask_navigation import Navigation

nav = Navigation(app)
nav.Bar('top', [
nav.Item('Home', 'index'),
nav.Item('Emotion analysis', 'emotion_post'),
nav.Item('Visualization', 'polynomial'),
nav.Item('Database Collections', 'get_all_databases'),
nav.Item('Database Personnel', 'get_all_personnel')
])


@app.route('/')
def index():
    return render_template("index.html")

my_dictionary={'Negative':'Sad', 'Positive':'Happy','Neutral':'Neutral'} # Defining a dictionary mapping each key to its appropriate value

@app.route('/emotion/') # By default the Emotions app page displays Happy Image
def emotion():
	return render_template("my_form.html",mood='Happy',form=MessageForm()) # my_form.html in templates folder maps the mood to relevant image


@app.route('/emotion/', methods=['POST'])
def emotion_post():
	msg = request.form['message']
	response = unirest.post("https://community-sentiment.p.mashape.com/text/",
	  headers={
	    "X-Mashape-Key": "6VWQcE5umumsh9oLsHfFlOseFGbDp1caaUKjsnj6PJRqxZKslv",
	    "Content-Type": "application/x-www-form-urlencoded",
    	"Accept": "application/json"
    	},
  		params={
    	"txt": msg
  		}
	)
	return render_template("my_form.html",mood=my_dictionary[response.body['result']['sentiment']],form=MessageForm()) # my_form.html in templates folder maps the mood to relevant image

