from flask import render_template, request, redirect, session
from todos_app import app
from todos_app.models.User import User

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "users.html", users=users )

@app.route( "/users/todos", methods=['GET'] )
def getAllUsersWithTodos():
    results = User.get_all_users_with_todos()
    return render_template( "fullusers.html", users=results )

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

@app.route( "/login", methods=['GET'] )
def displayLogin():
    loginError = ""
    if 'loginError' in session:
        loginError = session['loginError']
    return render_template( "index.html", loginError=loginError )

@app.route( "/authentication", methods=['POST'] )
def validateCredentials():
    userName = request.form['userName']
    userPassword = request.form['userPassword']
    identifier = request.form['identifier']
    print( 'Identifier', identifier )

    result = User.get_user_to_validate( userName, userPassword )

    if len( result ) == 1:
        session['userName'] = userName
        if 'loginError' in session:
            session.pop( 'loginError' )
        return redirect( '/home' )
    else:
        session['loginError'] = "Wrong credentials provided."
        return redirect( '/login' )

@app.route( "/logout", methods=['GET'] )
def closeSession():
    session.clear()
    responseObj = {
        'message' : 'logout successfully'
    }
    return responseObj
    #return redirect( '/login' )