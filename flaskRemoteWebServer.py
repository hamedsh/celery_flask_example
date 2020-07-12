from random import randint
from time import sleep

from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
app = Flask("test")
CORS(app)

@app.route("/error504", methods=["GET", "POST"])
def funcerr504():
    return jsonify({"error": "error type message"}), 504

@app.route("/error503", methods=["GET", "POST"])
def funcerr503():
    return jsonify({"error": "error type message"}), 503


@app.route("/ok", methods=["GET", "POST"])
def funcOk():
    num = request.args.get('num', '0')
    sleep(randint(2, 5))
    return jsonify({"message": "OK message", "val": int(num) * 9}), 200

app.run('0.0.0.0', 8008)
