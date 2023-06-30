from flask import Flask, templates
app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)