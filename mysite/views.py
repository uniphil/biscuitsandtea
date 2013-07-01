#!/bin/python2
from flask import render_template, safe_join, abort
from markdown import markdown
from mysite import app
from os import listdir
from os.path import isfile


@app.route("/")
def home():
    post_list = [p[:-3] for p in listdir(app.config['POSTS_FOLDER'])]
    return render_template("home.html", post_list=post_list)


@app.route("/posts/<postname>")
def post(postname):
    path = safe_join(app.config['POSTS_FOLDER'], postname + '.md')
    print(path)
    try:
        with open(path) as f:
            md = f.read()
    except IOError:
        abort(404)
    html_content = markdown(md, extensions=['codehilite', 'fenced_code'])
    return render_template("post.html", content=html_content)
