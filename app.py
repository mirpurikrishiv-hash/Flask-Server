from flask import Flask, request, render_template
import requests
import random

app = Flask(__name__)

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    res = requests.get(url).json()

    if res["type"] == "single":
        return res["joke"]
    else:
        return f"{res['setup']} - {res['delivery']}"

# Laughing emojis collection
LAUGH_EMOJIS = ["😂", "🤣", "😆", "😅", "😄", "😃", "🤪", "😋"]

def get_random_emoji():
    return random.choice(LAUGH_EMOJIS)

@app.route('/')
def joke():
    j = get_joke()
    emoji = get_random_emoji()
    return render_template('single_joke.html', joke=j, emoji=emoji)

@app.route("/many-jokes")
def jokes():
    count = int(request.args.get("count", 5))
    jokes_list = []
    for _ in range(count):
        jokes_list.append({
            'joke': get_joke(),
            'emoji': get_random_emoji()
        })
    return render_template('multiple_jokes.html', jokes=jokes_list)

# IMPORTANT: expose app as "app"