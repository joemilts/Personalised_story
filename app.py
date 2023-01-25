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
            max_tokens=1000
        )
        res = response.choices[0].text
        resl = slice(0, 350)
        resl1 = slice(350, 500)
        resl2 = slice(500, 650)
        result = res[resl]
        result1 = res[resl1]
        result2 = res[resl2]
        return redirect(url_for("about", result=result, result1=result1, result2=result2))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@ app.route("/about")
def about():
    result = request.args.get("result")
    result1 = request.args.get("result1")
    result2 = request.args.get("result2")
    return render_template("inde.html", result=result, result1=result1, result2=result2)


def generate_prompt(description, age, characters):
    return ' Kids story.' + f'Story about: {description}' + f' target age: {age}' + f'Include characters: {characters}'
