from flask import Flask
from todos_app import app
from todos_app.controllers import users_controller, todos_controller

if __name__ == "__main__":
    app.run( debug = True )

#this is a comment