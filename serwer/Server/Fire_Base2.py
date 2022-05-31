
import firebase_admin
from firebase_admin import credentials,firestore
cd = credentials.Certificate('C:\\Users\\micha\\Firebase\\paragon-scanner-firebase-adminsdk-n0fyt-1238f8bdb5.json')
# In the above line <path_to_generated_private_key>
# is a placeholder for the generate JSON file containing
# your private key.
firebase_admin.initialize_app(cd)
datab = firestore.client()
usersref = datab.collection(u'users')
docs = usersref.stream()
for doc in docs:
    print('{} : {}'.format(doc.id,doc.to_dict()))