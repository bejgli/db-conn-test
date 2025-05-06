import socket
from flask import Flask, request
import oracledb
from oracledb.exceptions import Error

import logging


app = Flask(__name__)


@app.route("/")
def index():
    try:
        conn = oracledb.connect(
            user=request.args.get("user"),
            password=request.args.get("pw"),
            dsn=request.args.get("dsn"),
        )
    except Error as e:
        logging.error(f"{e}")
        logging.info(socket.gethostbyname(socket.getfqdn()))

        return f"Err {e}"

    return f"Oracle Database version: {conn.version}"


if __name__ == "__main__":
    app.run(debug=True)
