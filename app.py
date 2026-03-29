from flask import Flask, request
import requests

app = Flask(__name__)

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    res = requests.get(url).json()

    if res["type"] == "single":
        return res["joke"]
    else:
        return f"{res['setup']} - {res['delivery']}"

@app.route('/')
def joke():
    return f"<h2>{get_joke()}</h2>"

@app.route("/many-jokes")
def jokes():
    count = int(request.args.get("count", 5))
    jokes_list = [get_joke() for _ in range(count)]
    return ''.join(f"<h2>{j}</h2>" for j in jokes_list)

# IMPORTANT: expose app as "app"