from os import name
from flask import *
import mysql.connector
from mysql.connector import connection
from mysql.connector import cursor
# 連線到資料庫


def connect_database():
    return mysql.connector.connect(
        user="root",
        password="12345678",
        host="localhost",
        database="website"
    )


app = Flask(__name__)


app.secret_key = "This is secrect key."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    conn = connect_database()
    cursor = conn.cursor()

    query = "SELECT * FROM member WHERE username = %s"
    cursor.execute(query, (username,))
    existing_member = cursor.fetchone()

    if existing_member != None:
        return redirect("error?message=帳號已被註冊")
    else:
        insertQuery = "INSERT INTO member(name,username,password) VALUES(%s,%s,%s)"
        cursor.execute(insertQuery, (name, username, password))
        conn.commit()
        return redirect("/")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    conn = connect_database()
    cursor = conn.cursor()

    query = "SELECT * FROM member WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    existing_member = cursor.fetchone()

    if (existing_member):
        session["id"] = existing_member[0]
        session["name"] = existing_member[1]
        session["username"] = existing_member[2]

        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")


@app.route("/member")
def member():
    if "username" in session:
        name = session["name"]

        conn = connect_database()
        cursor = conn.cursor()

        query = "SELECT member.username,message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY message.time DESC;"
        cursor.execute(query)
        messages = cursor.fetchall()
        formatted_messages = []
        for msg in messages:
            formatted_messages.append(f"{msg[0]}：{msg[1]}")
        conn.close()
        return render_template("member.html", name=name, message=formatted_messages)
    else:
        return redirect("/")


@app.route("/createMessage", methods=["POST"])
def createMessage():
    if "username" in session:
        name = session["name"]
        message = request.form["message"]

        conn = connect_database()
        cursor = conn.cursor()

        query = "INSERT INTO message (member_id, content) VALUES ((SELECT id FROM member WHERE username = %s), %s)"
        cursor.execute(query, (name, message))
        conn.commit()
        conn.close()

        return redirect("/member")
    else:
        return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("message", "發生錯誤")
    return render_template("error.html", message=message)


@app.route("/signout")
def signout():
    session.pop("id", None)
    session.pop("name", None)
    session.pop("username", None)
    return redirect("/")


app.run(port=3000)
