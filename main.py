from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index_page():
    user = {'username': 'Monea'}
    return render_template('index.html', title='Index Page', user=user)

@app.route('/login')
def login_page():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(debug=True)
