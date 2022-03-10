# #we started by importing the flask class
# from flask import Flask
# #then we make the instance of this class
# app = Flask(__name__)# this this the name of the application module oe package to passed arguments
# #route() decoratore is used to inform Flask which URL should activate our method
# @app.route("/")
# #this function returns the message should be show in the user's browser
# def home():
#     return " this is our first flask app."
# @app.route('/')
# def index():
#     return 'this is home page'
#
# @app.route('/hello')
# def hello():
#     return 'this is hello ,world page'
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return " this is our first flask app."
app.run(port=5000)

