from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    file_list = os.listdir("media")
    return render_template("index.html", list=file_list)

@app.route('/subdir/<path:path>')
def subdir(path):
    subdir_path = os.path.join("media", path)
    file_list = os.listdir(subdir_path)
    return render_template("subdir.html", list=file_list, subdir=path)

@app.context_processor
def utility_processor():
    def path(file_path):
        return os.path.isfile(file_path)
    return dict(path=path)


@app.route("/media/<path:path>")
def media(path):
    media_path = os.path.join("media", path)
    if os.path.isfile(media_path):
        with open(media_path, 'r') as file:
            content = file.read()
        return content
    else:
        return render_template('subdir.html')

@app.route('/static/<path:filepath>')
def static_render(filepath):
    return send_from_directory("static", filepath)

if __name__ == "__main__":
    app.run(debug=True)
