from flask import Blueprint, render_template, request 


view = Blueprint('view', __name__)



@view.route('/')
def home():
    return render_template("home.html", title = "Home")

@view.route('/om')
def om():
    return render_template("about.html", title = "About")

@view.route('/test')
def test():
    return render_template("htmltest.html", title = "Test")



