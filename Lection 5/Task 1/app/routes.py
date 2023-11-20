"""Flask routes"""

import bcrypt
from flask import request, redirect, render_template
from markupsafe import escape
import sqlalchemy

from app import app, db
from app.models import Messages, Users


@app.route("/")
def index():
    return redirect("/all", code=302)


@app.route("/all")
def all():
    return render_template("index.html", messages=get_all())


@app.route("/getAll")
def get_all():
    response = ""
    sql = sqlalchemy.select(
        Messages.messageDate, Users.username, Messages.message
    ).join(Users)
    for message in db.session.execute(sql):
        response += (
            f"[{message.messageDate}] {message.username}: {message.message}<br>\n"
        )
        print(response)
    return response


@app.route("/register", methods=["POST"])
def register():
    username = escape(request.form.get("username"))
    password = request.form.get("password")
    confirm = request.form.get("confirm")
    if password == confirm:
        try:
            db.session.add(
                Users(
                    username=username,
                    password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                )
            )
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return "Username already taken."
    else:
        return "Invalid password confirmation."
    return redirect("/all", code=302)


@app.route("/send", methods=["POST"])
def send():
    username = escape(request.form.get("username"))
    password = request.form.get("password")
    message = escape(request.form.get("message"))
    try:
        sql = sqlalchemy.select(Users.id, Users.password).where(
            Users.username == username
        )
        for user in db.session.execute(sql):
            if bcrypt.checkpw(password.encode(), user[1]):
                db.session.add(Messages(sender=user[0], message=message))
                db.session.commit()
    except Exception as e:
        print(f"Exception: {e}")
    return redirect("/all", code=302)
