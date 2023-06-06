import random
import re
import sys
from flask import Flask, render_template, render_template_string
from turbo_flask import Turbo
import threading
import time
import folium
from osm import m


app = Flask(__name__)
turbo = Turbo(app)
counter = 0

def update_load():
    with app.app_context():
        while True:
            time.sleep(3)
            turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

@app.route('/')
def index():
    return render_template('index.html')


@app.context_processor
def inject_load():

    # m = folium.Map()
    m.save("templates/map.html")
    return {"map": '1'}

if __name__ == "__main__":
    app.run(debug=True)