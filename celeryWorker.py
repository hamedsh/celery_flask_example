import os
import sys

from redis import Redis

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import celeryConfig
from celery import Celery
import time
import requests

app = Celery('celeryExample')
app.config_from_object(celeryConfig)

BASE_URL = 'http://127.0.0.1:8008/ok'
redisdb = Redis(db=4)


@app.task(name="getWebCelery")
def getWebCelery(key, num, method='GET', timeout=10):
    try:
        st = time.time()
        url = f'{BASE_URL}?num={num}'
        res = requests.request(method.upper(), f'{url}', timeout=timeout)
        load_time = time.time() - st
        load_time = round(load_time, 1)
        res.raise_for_status()
        redisdb.set(key, res.text)
    except requests.exceptions.Timeout as e:
        return 408, "timeout exception"
    except requests.HTTPError as e:
        return -1, "Failed to get fund status from MFR API: {}".format(str(e.errno))
    except Exception as e:
        return -2, e.args[0]
    return 200, load_time
