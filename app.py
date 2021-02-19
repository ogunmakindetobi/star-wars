from flask import Flask, render_template
import requests
import json

app = Flask (__name__)


@app.route('/', methods=['GET'])
def index():
    req = requests.get('http://swapi.dev/api/films/1/')
    data = json.loads(req.content)
    return render_template('index.html', data=data)


if __name__:
  app.run(host='0.0.0.0', debug=True)