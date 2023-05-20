from flask import Flask, render_template, redirect, url_for, request
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import openai

#openai.organization = ""
#openai.api_key = ""
#openai.Model.list()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('homepage.html')

if __name__ == "__main__":
    #port = int(os.environ.get('PORT', 13132))
    app.run(debug=True)