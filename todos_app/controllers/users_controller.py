from flask import render_template, request, redirect, session, jsonify, json
from flask_bcrypt import Bcrypt
from todos_app import app
from todos_app.models.User import User

bcrypt = Bcrypt(app)

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    
    #return jsonify( data ), 404
    return render_template( "users.html", users=users )

@app.route( "/users/todos", methods=['GET'] )
def getAllUsersWithTodos():
    results = User.get_all_users_with_todos()
    return render_template( "fullusers.html", users=results )

@app.route( "/users/add", methods=['POST'] )
def addUser():
    username = request.form['username']
    password = request.form['password']

    if User.validate_user_password( username, password ):
        encryptedPassword = bcrypt.generate_password_hash( password )
        newUser = User( username, encryptedPassword )
        result = User.add_user( newUser )
        print( result )
        return redirect( "/users" )
    else:
        print( "Something went wrong" )
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

    result = User.get_user_to_validate( userName )

    if len( result ) == 1:
        encryptedPassword = result[0]['password']

        if bcrypt.check_password_hash( encryptedPassword, userPassword ):
            session['userName'] = userName
            if 'loginError' in session:
                session.pop( 'loginError' )
            return redirect( '/home' )
        else:
            session['loginError'] = "Wrong credentials provided."
            return redirect( '/login' )
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

@app.route( "/api/users", methods=['GET'] )
def apiGetUsers():
    users = User.get_all_users( True )
    return jsonify( users ), 202

@app.route( "/api/users/delete/<username>", methods=['DELETE'] )
def apiDeleteUser( username ):
    print( request.data )
    print( request.data.decode('UTF-8') )
    usernameBody = json.loads(request.data.decode('UTF-8'))
    print( usernameBody['username'] ) 
    result = User.delete_user( username )
    if result == False:
        return {}, 406
    return jsonify( result ), 204

@app.route( "/api/users/add", methods=['POST'] )
def apiAddUser():
    print( request.form )
    username = request.form['userName']
    password = request.form['userPassword']
    encryptedPassword = bcrypt.generate_password_hash( password )
    newUser = User( username, encryptedPassword )
    result = User.add_user( newUser )
    # If username is duplicated send back a message with an error
    data = {
        "username" : username,
        "password" : password
    }
    return jsonify( data ), 201

@app.route( "/api/users/update", methods=['PUT'] )
def apiUpdateUserPassword():
    usernameBody = json.loads(request.data.decode('UTF-8'))
    print( usernameBody )
    encryptedPassword = bcrypt.generate_password_hash( usernameBody['password'] )
    data = {
        "password" : encryptedPassword,
        "username" : usernameBody['username']
    }
    result = User.update_user_password( data )
    # If username doesn't exists, we need to send another message possibly with an error status code
    return jsonify( {"message" : "user password updated"} ), 202
