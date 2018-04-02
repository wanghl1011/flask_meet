# from flask import Flask, render_template, request, redirect
from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

# app = Flask(__name__, template_folder='templates')
# app.debug = True


class LoginForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=1, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control','placeholder':"用户名"}

    )
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=1, message='密码长度必须大于%(min)d'),
            # validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
            #                   message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control','placeholder':'密码'}
    )



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         form = LoginForm()
#         return render_template('login.html', form=form)
#     else:
#         form = LoginForm(formdata=request.form)
#         if form.validate():
#             print('用户提交数据通过格式验证，提交的值为：', form.data)
#         else:
#             print(form.errors)
#         return render_template('login.html', form=form)

# if __name__ == '__main__':
    # l = LoginForm()
    # app.run()