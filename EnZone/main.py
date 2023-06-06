from flask import Flask, render_template_string
import folium


app = Flask(__name__)

@app.route("/")
def index():
    m = folium.Map()
    return m.get_root().render()




if __name__ == "__main__":
    app.run(debug=True)

