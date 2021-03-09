from flask import Flask, redirect, url_for, request, render_template, jsonify
from api import globalresult, excbot
import threading
import json
import asyncio

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', result=globalresult)


@app.route('/api', methods=['GET'])
def api():
    return jsonify(globalresult)

if __name__ == '__main__':
    threading.Thread(target=excbot, daemon=True).start()
    app.run(host='127.0.0.1', port='3000')
