import os
from flask import Flask
from flask import render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/')
def index():
    template = "index.html"
    return render_template(template)


if __name__ == '__main__':
    app.run(debug=True)
