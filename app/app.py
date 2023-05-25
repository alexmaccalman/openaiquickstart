import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="text-davinci-003", temperature=0.7):
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=100,
            temperature=temperature,
        )
        return response.choices[0].text
    except openai.OpenAIError as e:
        error_message = str(e)
        return f"Error: {error_message}"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        animal_result = get_completion(generate_animal_prompt(animal))
        return redirect(url_for("index", animal_result=animal_result))

    animal_result = request.args.get("animal_result")
    translation_result = request.args.get("translation_result")
    joke_result = request.args.get("joke_result")
    improve_result = request.args.get("improve_result")
    return render_template("index.html", 
                           animal_result=animal_result, 
                           translation_result=translation_result, 
                           joke_result=joke_result,
                           improve_result=improve_result
                           )


def generate_animal_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(animal.capitalize())


@app.route("/translate", methods=["POST"])
def translate():
    if request.method == "POST":
        text = request.form["text"]
        translation_result = get_completion(translate_text_to_spanish(text))
        return redirect(url_for("index", translation_result=translation_result))


def translate_text_to_spanish(text):
    return "Spanish translation of: " + text


@app.route("/joke", methods=["POST"])
def joke():
    if request.method == "POST":
        joke = request.form["joke"]
        joke_result = get_completion(generate_joke_prompt(joke))
        return redirect(url_for("index", joke_result=joke_result))


def generate_joke_prompt(joke):
    return """Write a joke about a {}""".format(joke.capitalize())
    
@app.route("/improve", methods=["POST"])
def improve():
    if request.method == "POST":
        improve = request.form["improve"]
        improve_result = get_completion(generate_improve_prompt(improve))
        return redirect(url_for("index", improve_result=improve_result))


def generate_improve_prompt(improve):
    return """I want you to act as a self-help book. You will provide me advice and tips
     on how to improve certain areas of my life, such as relationships, career or financial planning.
     For example, if I am struggling in my relationship with a significant other, you could suggest helpful communications
     techniques that can bring us closer together. The response should be at most 30 words Please provide me advice and tips the 
     following area of my life: {}""".format(improve.capitalize())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
