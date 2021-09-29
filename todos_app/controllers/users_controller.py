from flask import render_template
from todos_app import app
from todos_app.models.User import User

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    print( users )
    return render_template( "users.html", users=users )
