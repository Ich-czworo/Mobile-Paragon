
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate('C:\\Users\\micha\\Firebase\\paragon-scanner-firebase-adminsdk-n0fyt-1238f8bdb5.json')
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://paragon-scanner-default-rtdb.firebaseio.com/"
	})

ref = db.reference("/key1/key2/")
data = 	ref.get()
print(data)


#cred_obj = firebase_admin.credentials.Certificate('C:\\Users\\micha\\Firebase\\paragon-scanner-firebase-adminsdk-n0fyt-1238f8bdb5.json')
#default_app = firebase_admin.initialize_app(cred_obj, {
	#'databaseURL':databaseURL
	#})