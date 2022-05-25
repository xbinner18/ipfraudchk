from flask import Flask, jsonify
from ipfraud import database


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "<h1>Welcome to IP FRAUD CHK API</h1>\n<h1>How to use:</h1>\nJust pass the ip that u want to check in url."

@app.route("/<query>")
def data_(query):
    return jsonify(database(query))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
