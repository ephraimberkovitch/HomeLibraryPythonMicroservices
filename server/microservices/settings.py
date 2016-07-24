#! /usr/bin/env python
import json
from datetime import datetime

from flask import Flask
from flask import request

from crossdomain import crossdomain
import server.microservices.books.bl.books_operations;

app = Flask(__name__)

@app.route("/settings")
@crossdomain(origin='*')
def get_settings():
    return json.dumps(server.microservices.books.bl.settings_operations.get_all_settings())

@app.route("/update_setting")
@crossdomain(origin='*')
def update_setting():
    key = request.args['k']
    value = request.args['v']
    server.microservices.books.bl.settings_operations.update_setting(key, value)
    return'Ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5556)