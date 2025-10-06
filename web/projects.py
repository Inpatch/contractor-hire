from flask import Blueprint, render_template, request
import os
projects = Blueprint('projects', __name__)

@projects.route('/')
def projects_index():
    def find_files(directory):
        abs_directory = os.path.abspath(directory)
        file_list = []
        for root, dirs, files in os.walk(abs_directory):
            for file in files:
                file = file.replace(".html", "")
                file_list.append(file)
        return file_list

    return render_template("projects.html", title = "About", projects_school = find_files("web/templates/projects/school"), projects_personal = find_files("web/templates/projects/personal"))



@projects.route('/machine_learning')
def machine_learning():
    return render_template("projects/school/machine_learning.html", title = "Machine Learning")

@projects.route('/web_app')
def web_app():
    return render_template("projects/personal/web_app.html", title = "Web App")

