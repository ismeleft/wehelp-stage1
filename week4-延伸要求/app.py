import re
from flask import *
from werkzeug.exceptions import RequestURITooLarge

app = Flask(__name__)

# 使用session需要設定secret Key
app.secret_key = "any string "


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]

    if (account == "test" and password == "test"):
        session["account"] = account
        return redirect("/member")
    elif (account == "" or password == ""):
        return redirect("/error?message=帳號或密碼不得為空")
    else:
        return redirect("/error?message=請輸入正確的帳號和密碼")


@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")


# /error?message=錯誤訊息
@app.route("/error")
def error():
    message = request.args.get("message", "發生錯誤")
    return render_template("error.html", message=message)


@app.route("/signout")
def signout():
    del session["account"]
    return redirect("/")


@app.route("/square/<int:num>")
def square(num):
    result = num * num
    return render_template("calculate.html", result=result)


app.debug = True
app.run(port=3000)
