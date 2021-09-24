from flask import Flask, render_template, request, redirect, session

app = Flask( __name__ )
app.secret_key = "secret"

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
    return render_template( "index.html" )

@app.route( "/home", methods=['GET'] )
def displayHome():
    userName = session['userName']

    currentUserTodos = todos[ userName ]
    print( currentUserTodos )

    #if session['userName']:
    #    return render_template( "home.html" )
    #else:
    return render_template( "home.html", todos=currentUserTodos )

@app.route( "/authentication", methods=['POST'] )
def validateCredentials():
    userName = request.form['userName']
    userPassword = request.form['userPassword']
    for user in users:
        if user['username'] == userName and user['password'] == userPassword:
            session['userName'] = userName
            return redirect( '/home' )
    # Cover the scenario were the credentials are invalid
    return redirect( '/login' )

if __name__ == "__main__":
    app.run( debug = True )