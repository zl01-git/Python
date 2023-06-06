#!/usr/bin/env python
import itertools
import time
from flask import Flask, Response, redirect, request, url_for

app = Flask(__name__)
count = 0

@app.route('/')
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for i, c in enumerate(itertools.cycle('\|/-')):
                global count
                yield "data: %s %d\n\n" % (c, count)
                count += 1 
                time.sleep(.1)  # an artificial delay
        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='stream.html'))

if __name__ == "__main__":
    app.run(debug=True)