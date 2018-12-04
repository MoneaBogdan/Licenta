from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from config import Config, config
from forms import LoginForm
from flask_login import LoginManager, current_user, login_user
import pyrebase
import requests

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
#login = LoginManager(app)
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Monea'}
    return render_template('index.html', title='Index Page', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        #existing_user = auth.create_user_with_email_and_password(form.username.data, form.password.data)
        try:
            existing_user = auth.sign_in_with_email_and_password(form.username.data, form.password.data)
            #return auth.get_account_info(existing_user['idToken'])
        except requests.exceptions.HTTPError:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        #login_user(existing_user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login Page', form=form)

if __name__ == '__main__':
	app.run(debug=True)
