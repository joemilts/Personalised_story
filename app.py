import os
import re
import openai
from gtts import gTTS
from flask import Flask, redirect, render_template, request, url_for, Response
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

KEYVAULT_URI = "https://joemilton66.vault.azure.net/"

_credential = ClientSecretCredential(
    tenant_id="ce3d9b6f-0814-4c7c-815b-6850f1bcd4b3",
    client_id="386168dd-e3da-4d2a-a784-cd98bf3cb113",
    client_secret="sak8Q~hracnfF3w2.obj~n1_j7yZydUPEZ5JzcgZ"
)

_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credential)
secret = _sc.get_secret("openaisecret").value

app = Flask(__name__)
openai.api_key = _sc.get_secret("openaisecret").value


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
            # here mate you can specify how many characters you want to get
            max_tokens=1000
        )

        generated_story = response["choices"][0]["text"].strip()
        paragraphs = split_into_paragraphs(generated_story, 5)
        for i, paragraph in enumerate(paragraphs):
            variable_name = f"paragraph_{i+1}"
            globals()[variable_name] = paragraph

        paragraph = variable_name
        # and here to dived the the story into chapters you can change the value if you want

        result = paragraph_1
        result1 = paragraph_2
        result2 = paragraph_3
        result3 = paragraph_4
        result4 = paragraph_5
        

        # the audio function if you want to remove

        # here it ends
        return redirect(url_for("about", paragraph=paragraph, result=result, result1=result1, result2=result2, result3=result3, result4=result4))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/about")
def about():
    result = request.args.get("result")
    result1 = request.args.get("result1")
    result2 = request.args.get("result2")
    result3 = request.args.get("result3")
    result4 = request.args.get("result4")
    

    return render_template("inde.html",  result=result, result1=result1, result2=result2, result3=result3, result4=result4)


def generate_prompt(description, age, characters):
    return ' Kids story.' + f'Story about: {description}' + f' target age: {age}' + f'Include characters: {characters}' + f', Story length 380 word'


def split_into_paragraphs(text, num_paragraphs):
    # Split the text into sentences
    sentences = text.split('. ')

    # Calculate the number of sentences in each paragraph
    sentences_per_paragraph = len(sentences) // num_paragraphs

    # Split the sentences into paragraphs
    paragraphs = ['. '.join(sentences[i:i+sentences_per_paragraph])
                  for i in range(0, len(sentences), sentences_per_paragraph)]

    return paragraphs
