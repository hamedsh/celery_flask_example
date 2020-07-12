Run remote APi simulator (with random delay 2~5s). port 8008

`python3 flaskRemoteWebServer.py`

run main webServer that sends requests to remote API. port 8009

`python3 flaskLocalServer.py`

run multiple worker in multiple terminal window

`celery -A celeryWorker.app worker -n workerX@%h -P eventlet -c 200`

- replace workerX with optional identical worker name. ex: Worker1, Worke2, ...

run benchmark

`python3 bench.py`

responses are storing in redis db 4

architecture:


                                         ---> celeryWorker ----> flaskRemoteWebserver \
    bench ----> flaskLocalServer --redis----> celeryWorker ----> flaskRemoteWebserver --> redis 
          <----reg key---/               ---> celeryWorker ----> flaskRemoteWebserver /