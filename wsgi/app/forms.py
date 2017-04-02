from flask_wtf import Form
from wtforms import TextField, validators

class MessageForm(Form):
   message = TextField(u'This app is designed to print an emoticon corresponding to the emotional content (Happy, Sad, Neutral) in the sentence you type below. This is achieved with help of mashape through its RESTful APIs. Please type your sentence, make sure you type the words Happy, Sad, Neutral exactly with beginning letter in upper case', [validators.optional(), validators.length(max=200)]) # With help of wtforms TextField() the text sentence to appear in the Emotion apps page is setup



