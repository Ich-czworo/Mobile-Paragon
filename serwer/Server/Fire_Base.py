
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate('C:\\Users\\micha\\Firebase\\paragon-scanner-firebase-adminsdk-n0fyt-1238f8bdb5.json')
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://paragon-scanner-default-rtdb.firebaseio.com/"
	})

ref = db.reference("/key1/")
data = 	ref.get()
data2 = ref.child("key1").get()
data3 = db.reference("/key1/").child("key3").get()
data4 = ref.get()
print("key2/: ", data)
print("key2/.child: ", data2)
print("data3: ", data3)
print("data4: ", data4)

ref2 = db.reference("/key1/key19")
ref2.set(101)

ref3 = db.reference("/1/")
print("ref3:", ref3)
query = ref3.order_by_key().get()

print("query: ", query)