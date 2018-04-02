from flask import request, session, redirect, g, current_app, Blueprint,render_template
from test import LoginForm
from redis import Redis
from flask_session import RedisSessionInterface
# from flask.ext.session import Session
from views import app1
from views.utils import my_sql
conn = Redis(host='192.168.11.21',port=6379)
app1.session_interface = RedisSessionInterface(conn, key_prefix='__', use_signer=False)

# app1.config['SESSION_TYPE'] = 'redis'
# app1.config['SESSION_REDIS'] = Redis(host='192.168.11.21', port='6379')
# Session(app1)

@app1.route('/')
def hello_world():
    return 'Hello World!'

@app1.before_request
def logincheck():
    if request.path == "/" or request.path == "/login":
        return None
    login_key = session.get("login", None)
    if not login_key:
        return redirect("/login")
    else:
        pass

@app1.route("/login",methods=["GET","POST"],endpoint="login")
def Mylogin():
    if request.method == "GET":
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            username = form.data.get("name")
            pwd = form.data.get("pwd")
            user = my_sql.filter_user(username,pwd)
            if user:
                session["login"] = 1
                session["user"] = user["id"]
                return redirect("/app01/show/")
            else:
                error='用户名或密码错误'
                return render_template('login.html', form=form,error=error)
        else:
            print(form.errors)
            return render_template('login.html', form=form)




if __name__ == '__main__':
    app1.config.from_object("settings")
    # app.request_class
    # app1.__call__
    app1.run()

