#!/usr/bin/env python3.7

from flask import Flask, render_template, url_for, redirect, request
import mysql.connector as mydb

import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('demo.html')

@app.route('/register', methods=["POST"])
def register():
    try:
        data = request.data.decode('utf-8')
        data = json.loads(data)

        print(data)
        name = str(repr(data['name'])[1:-1])
        email = str(repr(data['email'])[1:-1])
        idm = str(repr(data['idm'])[1:-1])

        print(name)
        print(email)
        print(idm)

        with open("./users/%s-%s-%s.json" % (name, email, idm),'w') as f:
            f.write('{"name": "%s", "email": "%s", "idm": "%s"}' %(name, email, idm))

    except Exception as e:
        print(e)
        return 'error'

    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
