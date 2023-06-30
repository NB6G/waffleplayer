from flask import Flask, render_template, send_from_directory
import os
app = Flask(__name__)

@app.route('/')
def index():
    list = os.listdir("media")
    return render_template("index.html", list=list)

@app.route('/subdir/<path:path>')
def subdir(path):
    list = os.listdir(f"media/{path}")
    return render_template("subdir.html", list=list, subdir=path)

@app.route("/media/<path:path>")
def media(path):
    if os.path.isfile(f"media/{path}"):
        with open(f"media/{path}", 'r') as i:
            content = i.read()
        return content
    else:
        return render_template('subdir.html')
@app.route('/static/<path:filepath>')
#The static function is in use for some reason so here we use static render
def static_render(filepath):
    send_from_directory("static", filepath)
    

if __name__ == "__main__":
    app.run(debug=True)