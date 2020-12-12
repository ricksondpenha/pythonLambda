import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

print('Hello World!')
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(
    cred, {
        'apiKey': 'AIzaSyCC9vXRt5aGz03zvuq6FKEyKdit9a0tYsE',
        'authDomain': 'ecommerce-3ad25.firebaseapp.com',
        'databaseURL': 'https://ecommerce-3ad25.firebaseio.com',
        'projectId': 'ecommerce-3ad25',
        'storageBucket': 'ecommerce-3ad25.appspot.com',
        'messagingSenderId': '466121281687',
        'appId': '1:466121281687:web:b780635d4a792361cc59d2',
        'measurementId': 'G-SDDZF45DN7'
    })

db = firestore.client()

doc_ref = db.collection('users').document('PSU5Ql8Sr61W9riOwkrC')
doc_ref.set({'first': 'Ada', 'last': 'Lovelace', 'born': 1815}, merge=True)


def lambda_handler(event, context):
    print('Hello World!')
    return {'statusCode': 200, 'body': json.dumps('Hello from Lambda!')}
