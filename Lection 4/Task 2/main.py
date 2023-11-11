"""Character movement"""

from flask import Flask, render_template, redirect, request

app = Flask("Character movement")


def draw_field(x, y):
    """Draws a field with a character on specified coordinates"""
    field = ""
    for y_field in range(5, -6, -1):
        for x_field in range(-5, 6):
            if x_field == x and y_field == y:
                field += "@"
            else:
                field += "."
        field += "<br>"
    return field


def validate_coordinate(coordinate):
    """Validates a coordinate for overflow and returns a correct result"""
    while coordinate > 5:
        coordinate -= 11
    while coordinate < -5:
        coordinate += 11
    return coordinate


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with a form"""
    try:
        x = int(request.args.get("x"))
        y = int(request.args.get("y"))
    except (TypeError, ValueError):
        x = y = 0
    if request.method == "POST":
        print(request.form)
        if request.form.get("up"):
            y += 1
        if request.form.get("down"):
            y -= 1
        if request.form.get("left"):
            x -= 1
        if request.form.get("right"):
            x += 1

    x = validate_coordinate(x)
    y = validate_coordinate(y)

    print(x)
    print(y)

    if request.method == "POST":
        return redirect(f"/?x={x}&y={y}")

    return render_template("index.html", field=draw_field(x, y))


app.run(host="127.0.0.1")
