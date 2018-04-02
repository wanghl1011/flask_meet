from flask import Flask
from views.index import index
from views.meet import meetting
app1 = Flask("my_meet",template_folder="templates",static_folder='static',static_url_path='/static')


app1.register_blueprint(index)
app1.register_blueprint(meetting)




