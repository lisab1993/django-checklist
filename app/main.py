from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_view():
		return '<h1>I want to Deploy Flask to Heroku</h1>'
