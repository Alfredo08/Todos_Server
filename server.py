from flask import Flask, render_template, request, redirect, session
from todos_app import app
from todos_app.controllers import users_controller


users = [
    {
        "username" : "michael08",
        "password" : "pass123"
    },
    {
        "username" : "julie27",
        "password" : "pass456"
    },
    {
        "username" : "alfredo123",
        "password" : "pass555"
    }
]

todos = {
    "michael08" : [
        {
            "todo" : "Wash the dishes",
            "completed" : False
        },
        {
            "todo" : "Clean the house",
            "completed" : False
        }
    ],
    "julie27" : [
        {
            "todo" : "Go to the GYM",
            "completed" : True
        },
        {
            "todo" : "Make a birthday cake",
            "completed" : False
        }
    ],
    "alfredo123" : [
        {
            "todo" : "Explain POST method",
            "completed" : False
        },
        {
            "todo" : "Explain sessions",
            "completed" : False
        }
    ]
}

@app.route( "/login", methods=['GET'] )
def displayLogin():
    loginError = ""
    if 'loginError' in session:
        loginError = session['loginError']
    return render_template( "index.html", loginError=loginError )

@app.route( "/home", methods=['GET'] )
def displayHome():
    if 'userName' in session:
        userName = session['userName']
        currentUserTodos = todos[ userName ]
        print( currentUserTodos )
        return render_template( "home.html", todos=currentUserTodos )
    else:
        return render_template( "index.html" )

@app.route( "/authentication", methods=['POST'] )
def validateCredentials():
    userName = request.form['userName']
    userPassword = request.form['userPassword']
    identifier = request.form['identifier']
    print( 'Identifier', identifier )
    for user in users:
        if user['username'] == userName and user['password'] == userPassword:
            session['userName'] = userName
            if 'loginError' in session:
                session.pop( 'loginError' )
            return redirect( '/home' )
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


if __name__ == "__main__":
    app.run( debug = True )