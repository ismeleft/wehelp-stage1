from flask import *

app = Flask(__name__)

# 使用session需要設定secret Key
app.secret_key = "This is secrect key."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    # 如果帳號密碼都是test則進到會員頁面
    if (account == "test" and password == "test"):
        # 輸入正確的話，要在session中紀錄會員資訊
        session["account"] = account
        return redirect("/member")
    # 如果帳號密碼其中一個為空，跳轉至錯誤頁面並提示用戶
    elif (account == "" or password == ""):
        return redirect("/error?msg=帳號或密碼不得為空")
    # 如果帳號密碼錯誤，跳轉至錯誤頁面並提示用戶
    else:
        return redirect("/error?msg=請輸入正確的帳號和密碼")


@app.route("/member")
def member():
    # 如果session中有會員帳號資料才導向會員頁面，避免有心人士直接打網址
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")


@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤")
    return render_template("error.html", message=message)


@app.route("/signout")
def signout():
    # 移除session會員中的資訊
    del session["account"]
    return redirect("/")


app.run(port=3000)
