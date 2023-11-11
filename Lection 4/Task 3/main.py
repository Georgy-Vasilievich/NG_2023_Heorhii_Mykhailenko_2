"""Image gallery in Flask"""

from flask import Flask, render_template, request
from os.path import exists

app = Flask("Image gallery")

@app.route("/")
def index():
    """Main page"""

    number = request.args.get("number")

    if not number or not exists(f"static/{number}.png"):
        number = 1
    else:
        next = int(number) + 1
        previous = int(number) - 1
        if not exists(f"static/{previous}.png"):
            previous = False
        if not exists(f"static/{next}.png"):
            next = False

    return render_template("index.html", number=number, previous=previous, next=next)

app.run(host="127.0.0.1")
