from flask import Flask, request, jsonify
import os
from db import save_request_data, count_requests

app = Flask(__name__)
healthy = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route("/")
def hello():
    global healthy
    if healthy:
        return f"Hello from {os.environ['HOST']}!\n"
    else:
        return "Unhealthy", 503


@app.route("/save", methods=["POST"])
def save():
    body = request.form
    save_request_data(body)
    return "Ok"


@app.route("/count", methods=["GET"])
def count():
    return jsonify(total_orders_processed=count_requests())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
