### @petertahinduka ######

### This file fires up the ShopEasy Application ###

from flask import Flask, render_template, json, request
from flask_login import LoginManager
from user import get_user

login_manager = LoginManager()

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('shopeasy_index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signin.html')


@app.route('/showHome')
def showHome():
    return render_template('home.html')

def load_user(user_id):
    return get_user(user_id)

def create_app():
    app = Flask(__name__)
    #app.config.from_object('settings')
    #app.register_blueprint(site)

    #lm.init_app(app)
    #lm.login_view = 'site.login_page'

   # app.store = Store()

    return app


#@app.route('/signUp',methods=['POST','GET'])
#def signUp():
    #try:
       # _name = request.form['inputName']
        #_email = request.form['inputEmail']
        #_password = request.form['inputPassword']
        
if __name__ == "__main__":
    app.run(port=5002)
