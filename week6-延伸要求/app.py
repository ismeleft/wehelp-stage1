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
        session["username"] = username

        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")


@app.route("/member")
def member():
    if "username" in session:
        name = session["name"]

        conn = connect_database()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT member.username,message.id,message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY message.time DESC;"
        cursor.execute(query)
        messages = cursor.fetchall()
        conn.close()
        return render_template("member.html", name=name, message=messages)
    else:
        return redirect("/")


@app.route("/createMessage", methods=["POST"])
def createMessage():
    if "username" in session:
        name = session["name"]
        message = request.form["message"]

        conn = connect_database()
        cursor = conn.cursor(dictionary=True)

        query = "INSERT INTO message (member_id, content) VALUES ((SELECT id FROM member WHERE username = %s), %s)"
        cursor.execute(query, (name, message))
        conn.commit()
        conn.close()

        return redirect("/member")
    else:
        return redirect("/")


@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    msg_id = request.data.decode("utf-8")
    print("收到前端留言刪除的id", msg_id)
    if msg_id:
        sql = "DELETE FROM message WHERE id=%s"
        conn = connect_database()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(sql, (msg_id,))
        conn.commit()
        conn.close()
        return "ok"

    return "刪除請求失敗"


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
