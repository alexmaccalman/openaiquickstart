import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message["content"]
    except openai.error.RateLimitError as e:
        # Handle rate limit error
        error_message = f"That model is currently overloaded with other requests. Please try again later."
        print(e)  # Print the error message
        return error_message


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            animal = request.form["animal"]
            animal_result = get_completion(generate_animal_prompt(animal))
            return redirect(url_for("index", animal_result=animal_result))
        except KeyError:
            # Handle missing 'animal' field error
            error_message = "Invalid request. Please enter a valid animal."
            return render_template("error.html", error_message=error_message)

    animal_result = request.args.get("animal_result")
    translation_result = request.args.get("translation_result")
    joke_result = request.args.get("joke_result")
    return render_template("index.html", animal_result=animal_result,
                           translation_result=translation_result,
                           joke_result=joke_result)


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
        try:
            text = request.form["text"]
            translation_result = get_completion(translate_text_to_spanish(text))
            return redirect(url_for("index", translation_result=translation_result))
        except KeyError:
            # Handle missing 'text' field error
            error_message = "Invalid request. Please enter a valid text to translate."
            return render_template("error.html", error_message=error_message)


def translate_text_to_spanish(text):
    return "Spanish translation of: " + text


@app.route("/joke", methods=["POST"])
def joke():
    if request.method == "POST":
        try:
            joke = request.form["joke"]
            joke_result = get_completion(generate_joke_prompt(joke))
            return redirect(url_for("index", joke_result=joke_result))
        except KeyError:
            # Handle missing 'joke' field error
            error_message = "Invalid request. Please enter a valid joke topic."
            return render_template("error.html", error_message=error_message)


def generate_joke_prompt(joke):
    return """Write a joke about a {}""".format(joke.capitalize())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
