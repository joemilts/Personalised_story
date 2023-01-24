import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        description = request.form["description"]
        age = request.form["age"]
        characters = request.form["characters"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(description, age, characters),
            temperature=0.4,
            max_tokens=500
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

@app.route("/about")
def about():
    result = request.args.get("result")
    return render_template("about.html", result=result)

def generate_prompt(description, age, characters):
    return ' Kids story.' + f'Story about: {description}' + f' target age: {age}' + f'Include characters: {characters}'

    