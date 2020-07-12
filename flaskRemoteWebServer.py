from random import randint
from time import sleep

from flask import Flask, jsonify, request

# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)

app = Flask("test")


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


app.run('0.0.0.0', 8008, debug=False)
