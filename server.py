from flask import Flask, render_template, request, redirect, session
from todos_app import app
from todos_app.controllers import users_controller, todos_controller

if __name__ == "__main__":
    app.run( debug = True )