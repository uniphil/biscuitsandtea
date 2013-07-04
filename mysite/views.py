#!/bin/python2
from flask import render_template, render_template_string, safe_join, abort
from markdown import markdown
from mysite import app
from os import listdir
from os.path import isfile

from markdown.preprocessors import Preprocessor

@app.route("/")
def home():
    posts = [open_markdown(p) for p in listdir(app.config['POSTS_FOLDER'])]
    posts = [parse_markdown(p) for p in posts]
    return render_template("home.html", posts=posts)


@app.route("/posts/<postname>")
def post(postname):
    path = safe_join(app.config['POSTS_FOLDER'], postname + '.md')
    print(path)
    md = open_markdown(postname + '.md')
    if md == 404:
        abort(404)
    else:
        html_content = parse_markdown(md)
        return render_template("post.html", content=html_content)


@app.route(app.config['MEDIA_URL']+"<filename>")
def media(filename):
    try:
        with open(safe_join(app.config['MEDIA_FOLDER'], filename)) as f:
            return f.read()
    except IOError:
        abort(404)

def open_markdown(filename):
    path = safe_join(app.config['POSTS_FOLDER'], filename)
    try:
        with open(path) as f:
            return f.read()
    except IOError:
        return 404

def parse_markdown(md):
    md = render_template_string(md, MEDIA_URL=app.config['MEDIA_FOLDER'])
    html_content = markdown(md, extensions=['codehilite', 'fenced_code',
                                            'attr_list', 'abbr'])
    return html_content


class PreviewPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        pre = False
        for line in lines:
            if line.startswith("\%\%\%"):
                if not pre:
                    pre = True
                else:
                    pre = False
                continue

            if pre:
                new_lines.append(line)
        if not new_lines:
            return lines
        else:
            return new_lines

