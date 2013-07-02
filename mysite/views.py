#!/bin/python2
from flask import render_template, render_template_string, safe_join, abort
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
    md = render_template_string(md, MEDIA_URL=app.config['MEDIA_FOLDER'])
    html_content = markdown(md, extensions=['codehilite', 'fenced_code',
                                            'attr_list'])
    return render_template("post.html", content=html_content)


@app.route(app.config['MEDIA_URL']+"<filename>")
def media(filename):
    try:
        with open(safe_join(app.config['MEDIA_FOLDER'], filename)) as f:
            return f.read()
    except IOError:
        abort(404)
