`python3 flaskRemoteWebServer.py`

`python3 flaskLocalServer.py`

run multiple worker in multiple terminal window

`celery -A celeryWorker.app worker -n workerX@%h -P eventlet -c 200`

- replace workerX with optional identical worker name. ex: Worker1, Worke2, ...

run benchmark

`python3 bench.py`

architecture:


                                         ---> celeryWorker ----> flaskRemoteWebserver \
    bench ----> flaskLocalServer --redis----> celeryWorker ----> flaskRemoteWebserver --> redis 
          <----reg key---/               ---> celeryWorker ----> flaskRemoteWebserver /