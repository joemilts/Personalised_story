import os
import re
import openai
from gtts import gTTS
from flask import Flask, redirect, render_template, request, url_for, Response

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
            # here mate you can specify how many characters you want to get
            max_tokens=1500
        )
        # and here to dived the the story into chapters you can change the value if you want
        res = response.choices[0].text
        resl = slice(0, 340)
        resl1 = slice(340, 680)
        resl2 = slice(680, 920)
        resl3 = slice(920, 1500)
        result = res[resl]
        result1 = res[resl1]
        result2 = res[resl2]
        result3 = res[resl3]

        def read_text(text):

            tts = gTTS(text=text, lang='en')
            tts.save("audio/audio.wav")

        def read_text1(text):

            tts = gTTS(text=text, lang='en')
            tts.save("audio/audio1.wav")

        def read_text2(text):

            tts = gTTS(text=text, lang='en')
            tts.save("audio/audio2.wav")

        def read_text3(text):

            tts = gTTS(text=text, lang='en')
            tts.save("audio/audio3.wav")

        def read_text4(text):

            tts = gTTS(text=text, lang='en')
            tts.save("audio/audio4.wav")
        audio_file = read_text(res)
        audio_file1 = read_text1(result)
        audio_file2 = read_text2(result1)
        audio_file3 = read_text3(result2)
        audio_file4 = read_text4(result3)

        return redirect(url_for("about", result=result, result1=result1, result2=result2, result3=result3))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/about")
def about():
    result = request.args.get("result")
    result1 = request.args.get("result1")
    result2 = request.args.get("result2")
    result3 = request.args.get("result3")
    return render_template("inde.html", result=result, result1=result1, result2=result2, result3=result3)


@app.route("/wav")
def streamwav():
    def generate():
        with open("audio/audio.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


@app.route("/wav1")
def streamwav1():
    def generate():
        with open("audio/audio1.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


@app.route("/wav2")
def streamwav2():
    def generate():
        with open("audio/audio2.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


@app.route("/wav3")
def streamwav3():
    def generate():
        with open("audio/audio3.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


@app.route("/wav4")
def streamwav4():
    def generate():
        with open("audio/audio4.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")


def generate_prompt(description, age, characters):
    return ' Kids story.' + f'Story about: {description}' + f' target age: {age}' + f'Include characters: {characters}'
