#!/bin/python2
from flask import render_template, safe_join, abort
from markdown import markdown
from mysite import app


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/posts/<postname>")
def post(postname):
    path = safe_join(app.config['POSTS_FOLDER'], postname + '.md')
    print(path)
    try:
        with open(path) as f:
            md = f.read()
    except IOError:
        abort(404)
    html_content = markdown(md)
    return render_template("post.html", content=html_content)
