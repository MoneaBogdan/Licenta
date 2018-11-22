from firebase import firebase

firebase = firebase.FirebaseApplication('https://licenta-b5e5b.firebaseio.com', None)
#result = firebase.put('users', '6', {'Nume': 'Miclea', 'Prenume': 'Mihaiiii'})
#result = firebase.delete('users', '6')
result = firebase.get('users', None)

for r in result[1:]:
    print r
