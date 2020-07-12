from uuid import uuid4

from flask import Flask, request
from celeryWorker import *

app = Flask(__name__)
redisdb = Redis(db=4)


@app.route('/getapi')
def getApi():
    num = request.args.get('num', 0)
    method = request.args.get('mathod', 'GET')
    timeout = request.args.get('timeout', 10)
    key = uuid4()
    # print(key)
    getWebCelery.delay(key, num, method, timeout)
    return {"key": key}


if __name__ == '__main__':
    app.run('0.0.0.0', 8009)
