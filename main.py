from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from config import Config
from forms import LoginForm
from flask_login import LoginManager, current_user, login_user
from firebase import firebase


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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        firebase = firebase.FirebaseApplication('https://licenta-b5e5b.firebaseio.com', None)
        results = firebase.get('users', None)
        for result in results[1:]:
            if form.username.data != result['Nume'] or form.password.data != result['Password']:
                flash('Invalid username or password')
                return redirect(url_for('login'))
            # login_user(result['Nume'], remember=form.remember_me.data)
            # return redirect(url_for('index'))
    return render_template('login.html', title='Login Page', form=form)

if __name__ == '__main__':
	app.run(debug=True)
