from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from config import Config
from forms import LoginForm
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
login = LoginManager(app)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Monea'}
    return render_template('index.html', title='Index Page', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Login Page', form=form)

if __name__ == '__main__':
	app.run(debug=True)
