from flask import stream_with_context, request, Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def generate_large_csv():
    def generate():
        for row in "adadwedweojfgifb2oibo2nvo":
            yield f"{','.join(row)}\n"
    return generate(), {"Content-Type": "text/csv"}


if __name__ == "__main__":
    app.run(debug=True)