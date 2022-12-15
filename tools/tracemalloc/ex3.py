from flask import Flask, jsonify
import time


import tracemalloc


app = Flask(__name__)


@app.route('/')
def line_test():

    for item in range(5):
        print(item)
        time.sleep(0.2)

    snapshot2 = tracemalloc.take_snapshot()
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    for stat in top_stats[:10]:
        print(stat)

    return jsonify({'code': 200})


if __name__ == '__main__':
    tracemalloc.start()
    snapshot1 = tracemalloc.take_snapshot()
    app.run()