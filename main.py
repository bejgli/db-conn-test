from flask import Flask, request
import oracledb
import os

import logging


app = Flask(__name__)


@app.route("/")
def index():
    try:
        dsn = os.environ["CONNECTION_STRING"]

        conn = oracledb.connect(
            user=request.args.get("user"),
            password=request.args.get("pw"),
            dsn=dsn,
        )
    except Exception as e:
        logging.error(f"{e}")
        return f"Err {e}"

    return f"Oracle Database version: {conn.version}"


if __name__ == "__main__":
    app.run(debug=True)
