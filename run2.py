import threading
import time

import requests
from flask import Flask

app = Flask(__name__)


@app.route("/trigger_alarm")
def trigger_alarm():
    return "trigger_alarm"


def kill_alarm():
    requests.get('http://raberry1:5000/kill_alarm')


def start_runner():
    def loop():
        not_started = True
        while not_started:
            print('In start loop')
            # TODO add button loopy loop
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=loop)
    thread.start()


if __name__ == "__main__":
    start_runner()
    app.run()
