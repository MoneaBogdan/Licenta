from firebase import firebase
import pyrebase
from config import config
import requests

# firebase = firebase.FirebaseApplication('https://licenta-b5e5b.firebaseio.com', None)
# result = firebase.put('users', '6', {'Nume': 'Miclea', 'Prenume': 'Mihaiiii'})
# result = firebase.delete('users', '6')
# result = firebase.get('users', None)

# for r in result[1:]:
#     print r

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


email = "bogdy_monea@yahoo.com"
password = "init_4321"

try:
    print(auth.sign_in_with_email_and_password(email, password))
    auth.get_account_info(existing_user['idToken'])
    data = {
        "email": email,
        "password": password,
        "username": "bogdy"
    }
    results = db.child("Users").push(data, existing_user['idToken'])
except requests.exceptions.HTTPError:
    print (existing_user)
