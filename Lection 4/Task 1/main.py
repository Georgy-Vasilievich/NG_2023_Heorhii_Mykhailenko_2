"""Calculator in Flask"""

from flask import Flask, render_template, request

app = Flask("Calculator")

@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with a form"""
    result = None
    if request.method == "POST":
        try:
            number_one = float(request.form.get("number_one"))
            number_two = float(request.form.get("number_two"))
            action = request.form.get("action")
            match action:
                case '+':
                    result = number_one + number_two
                case '-':
                    result = number_one - number_two
                case '*':
                    result = number_one * number_two
                case '/':
                    result = number_one / number_two if number_two != 0 else "Division by zero."
                case _:
                    result = "Unknown action."
        except (TypeError, ValueError):
            result = "Incorrect numbers entered."
    return render_template("index.html", result=result)

app.run(host="127.0.0.1")
