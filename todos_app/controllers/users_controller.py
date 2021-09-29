from flask import render_template, request, redirect
from todos_app import app
from todos_app.models.User import User

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "users.html", users=users )

@app.route( "/users/add", methods=['POST'] )
def addUser():
    username = request.form['username']
    password = request.form['password']

    newUser = User( username, password )
    result = User.add_user( newUser )
    print( result )
    return redirect( "/users" )

@app.route( "/users/delete", methods=['POST'] )
def deleteUser():
    username = request.form['deleteUsername']
    result = User.delete_user( username )
    print( result )
    return redirect( "/users" )