import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

config = {
    "apiKey": "AIzaSyDP2Z2XQ7N_jD9ZAdQtB8MCPhSwC1qK-IM",
    "authDomain": "licenta-b5e5b.firebaseapp.com",
    "databaseURL": "https://licenta-b5e5b.firebaseio.com",
    "projectId": "licenta-b5e5b",
    "storageBucket": "licenta-b5e5b.appspot.com",
    "messagingSenderId": "837391391848"
}
