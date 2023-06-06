from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    server_message = ""
    client_message = ""
    if request.method == "POST":
        client_message = request.form.get("message")

    if client_message == "hi":
        server_message = "hello"
    elif client_message != "":
        server_message = "How are you?"
    return render_template("ind.html", message="")


if __name__ == "__main__":
    app.run(debug=True)