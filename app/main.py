from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
  return "<h1>Deneme heroku 2...</h1>"
