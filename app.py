import sqlite3
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("projects.html")


# Function to connect to database in sqlite3
def get_db_connection():
    conn = sqlite3.connect('database/sitio.db')
    conn.row_factory = sqlite3.Row
    return conn


class Project():

    # Define our constructor
    def __init__(self, projects, users):
        self.projects = proyectos
        self.users = usuarios

    # Function to bring all projects
    def get_proyectos():
        connect = get_db_connection()
        projects = connect.execute("SELECT * FROM project").fetchall()
        connect.close()
        return projects

    # Function to bring all projects
    @app.route('/proyecto/')
    def proyecto():
        projects = Project.get_proyectos()
        return render_template("projects.html", projects=projects)

    # Function to bring all projects the project_id
    def get_project(project_id):
        connect = get_db_connection()
        proyectos = connect.execute('SELECT * FROM project WHERE id = ?', (project_id,)).fetchone()
        connect.close()
        return json.dumps(proyectos, default=list)

    # Function to show all projects from one particular project_id
    @app.route('/proyecto/<id_proyecto>')
    def project(project_id):
        project = get_project(project_id)
        return render_template('project.html', project=project)

    # Function to join users with role
    def get_user_role_inner_join_all():
        connect = get_db_connection()
        users_role = connect.execute(
            "SELECT user_id,username,password,user_full_name,role_id,name,description FROM user INNER JOIN user_role_association_table INNER JOIN role").fetchall()
        connect.close()
        usuarios = []
        for usuario in users_role:
            u = {}
            u['user_id'] = usuario['user_id']
            u['username'] = usuario['username']
            u['password'] = usuario['password']
            u['user_full_name'] = usuario['user_full_name']
            u['role_id'] = usuario['role_id']
            u['name'] = usuario['name']
            u['description'] = usuario['description']
            usuarios.append(u)
        return usuarios


        @app.route('/user/')
        def crear_objecto():
            users = Project.get_user_role_inner_join_all()
            projects = Project.get_proyectos()
            return json.dumps({'projects': projects, 'users': users}, default=list)


if __name__ == '__main__':
    app.run(debug=True)
    proyecto.run(debug=True)
