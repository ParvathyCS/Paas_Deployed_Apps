# Deploying apps : Written using Python programming language and FLASK web framework


### Sentiment analysis

### Visualization of a polynomial

### Connecting to Mongodb database

Demo URL where the apps are served
=================================

You can customize URL according to your need. Demonstration has been provided in the URL which is served securely:
https://pcs30apitest1-parvathy.apps.devcloud.eecs.qmul.ac.uk/

The plane http also works.

This git repository includes the relevant files required to deploy apps written in python and flask.

Repo layout
===========
wsgi/ - Externally exposed wsgi code goes
wsgi/static/ - Public static content gets served here
libs/ - Additional libraries
data/ - For not-externally exposed wsgi code
setup.py - Standard setup.py, specify module/package which needs to be installed
../data - For persistent data (also env var: OPENSHIFT_DATA_DIR)
.openshift/action_hooks/pre_build - Script that gets run every git push before the build
.openshift/action_hooks/build - Script that gets run every git push as part of the build process (on the CI system if available)
.openshift/action_hooks/deploy - Script that gets run every git push after build but before the app is restarted
.openshift/action_hooks/post_deploy - Script that gets run every git push after the app is restarted

wsgi/app
=====
* This (app) folder consists of:

* various python scripts related to emotion app, visualization app and database app [_init_.py,simple.py,views2.py,forms.py,database.py]

* static folder containing the image folder for emotion app which describes Happy, Sad, Neutral emotions as follows:

<br>
<img src = "wsgi/app/static/img/Happy_face.jpeg" height="60" width="60">

<img src = "wsgi/app/static/img/Sad_face.jpeg" height="60" width="60">

<img src = "wsgi/app/static/img/Neutral_face.jpeg" height="60" width="60">
</br>

* templates folder consists of base.html, embed.html, index.html, my_form.html files which supports in setting the appearance of all the pages

Application of various apps
===========================

**Emotion app** maps the emotional content in the user typed sentence to an appropriate image. This is achieved with the help of mashape through its RESTful API services.# Please type Happy,Sad and Neutral with starting letter in upper case.

**Visualization app** plots the polynomial expression y=x^2 depending on the user entered values and colors. The colors should be selected from list here (Red, Green, Blue, Black). Please type the color *exactly* as given here, it is case sensitive. The values entered must be integers and From value should be less than To value.

**Database app** performs basic functionality of adding MongoDB database to the app.


Contact
=======

## Email - ec16022@qmul.ac.uk


Author
======

Parvathy Chittur SubramanianPrasad




