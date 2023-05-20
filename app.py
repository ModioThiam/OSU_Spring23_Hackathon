from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os
import openai
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env
import os
import json


#openai.organization = ""
openai.api_key = os.getenv("API_KEY")
#openai.Model.list()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'

# Initialize the database
db = SQLAlchemy(app)


@app.route('/recipe', methods=['POST', 'GET'])
def homepage():
    if request.method == "GET":
        return render_template('homepage.html')
    elif request.method == "POST":

        user_input = request.form["ingredients"]

        prompt = """
        Give me a popular recipe represented as a Python dictionary object that includes 3 or less similar ingredients
        of these ingredients: """ + user_input + """ Give me only the Python object. Your output must always be in valid Python dicionary format.
        Example:
        {
            "recipeName": <Put recipe name here>,
            "ingredients": <List ingredients here>,
            "instructions": <List instructions here>
        
        }
        """

        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0
        )

        response = response.choices[0].text.strip()
        res = json.loads(response)
        recipeName = res["recipeName"]
        ingredients = res["ingredients"]
        instructions = res["instructions"]    
    
        return render_template('apitest.html', recipeName=recipeName, ingredients=ingredients, instructions=instructions)



if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 13132))
    app.run(debug=True)
