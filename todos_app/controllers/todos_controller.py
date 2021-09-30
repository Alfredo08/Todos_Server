from flask import session, render_template
from todos_app import app
from todos_app.models.Todo import Todo

@app.route( "/home", methods=['GET'] )
def displayHome():
    if 'userName' in session:
        userName = session['userName']
        results = Todo.get_todos_from_user( userName )
        return render_template( "home.html", todos=results )
    else:
        return render_template( "index.html" )