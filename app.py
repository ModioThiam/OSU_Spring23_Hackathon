from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os
import openai
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env
import os
import json
import re


#openai.organization = ""
openai.api_key = os.getenv("API_KEY")
#openai.Model.list()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'

# Initialize the database
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == "GET":
        return render_template('homepage.html')
    elif request.method == "POST":

        user_input = request.form["ingredients"]

        prompt = """
        Give me a popular recipe represented as a JSON object that includes 3 or less similar ingredients of these
        ingredients: """ + user_input + """ Give me only the json object. Your output must always be in valid JSON format ensure there is no unterminated string.
        I only want the object, do not talk to me. Do not use the word Example in your response.
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
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0
        )

        def extract_recipe_info(json_str):
            recipe_info = {}
            recipe_dict = json.loads(json_str)

            # Extract recipe name
            recipe_info["recipeName"] = recipe_dict["recipeName"]

            # Extract instructions
            instructions_str = recipe_dict["instructions"]
            recipe_info["instructions"] = instructions_str

            # Extract ingredients as a list
            ingredients_list = recipe_dict["ingredients"]
            recipe_info["ingredients"] = ingredients_list

            return recipe_info

        response_1 = response.choices[0].text.strip()

        recipe_info = extract_recipe_info(response_1)

        recipeName = recipe_info["recipeName"]
        instructions = recipe_info["instructions"]
        ingredients = recipe_info["ingredients"]

        ingredientTitle = "Ingredients: "
        instructionTitle = "Instructions: "

        scroll_position = request.args.get('scroll_position', 0)

        return render_template('homepage.html', recipeName=recipeName, instructions=instructions, ingredients=ingredients, ingredientTitle=ingredientTitle, instructionTitle=instructionTitle, scroll_position=scroll_position)



if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 13132))
    app.run(debug=True)
