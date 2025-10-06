from flask import Blueprint, render_template
import json

api = Blueprint('api', __name__)



@api.route('/')
def index():
    return {"message":"api is not configured yet"}
@api.route('/test')
def test():
    return render_template("apitest.html", title = "Test")