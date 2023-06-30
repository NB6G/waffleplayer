from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/static/<path:filepath>')
#The static function is in use for some reason so here we use static render
def static_render(filepath):
    send_from_directory("static", filepath)
    



if __name__ == "__main__":
    app.run(debug=True)