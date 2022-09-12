import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime


def init_fb_app():
	cred = credentials.Certificate(
		'C:\\Users\\micha\\Firebase\\paragon-scanner-firebase-adminsdk-n0fyt-1238f8bdb5.json')
	default_app = firebase_admin.initialize_app(cred, {
		'databaseURL': "https://paragon-scanner-default-rtdb.firebaseio.com/"
	})


def save_scanned_receipt(user_id, scanned_receipt):
	date = datetime.now()
	date_str = date.strftime("%Y-%m-%d")
	hour = date.strftime("%H:%M:%S")
	ref = db.reference('/' + user_id).child(date_str).child(hour)

	for (index, word) in enumerate(scanned_receipt):
		print(index + 1, " ", word)
		ref.child(str(index)).set(word)

	#for product, value in scanned_receipt.items():
		#ref.child(product).set(value)


def get_data(user_id):
	db_data = db.reference("/" + user_id).get()
	return db_data


def get_data_between_two_dates(user_id, date_lower, date_upper):
	data = db.reference("/" + user_id).get()

	output_data = {}
	for (key, value) in data.items():
		if is_earlier(key, date_lower) and is_later(key, date_upper):
			for (date, receipt) in value.items():
				for (product, price) in receipt.items():
					if product in output_data.keys():
						output_data[product] += price
					else:
						output_data[product] = price

	output = ""
	for (key, value) in output_data.items():
		output += str(key) + " - " + str(value) + "\n"
	return output

def is_earlier(date, date_lower):
	date = date.split("-")
	date_lower = date_lower.split("-")

	date = [int(x) for x in date]
	date_lower = [int(x) for x in date_lower]

	answer = False
	for i in range(3):
		if date[i] > date_lower[i]:
			answer = True
			break

	return answer


def is_later(date, date_upper):
	date = date.split("-")
	date_upper = date_upper.split("-")

	date = [int(x) for x in date]
	date_upper = [int(x) for x in date_upper]

	answer = False
	for i in range(3):
		if date[i] < date_upper[i]:
			answer = True
			break
		elif date[i] > date_upper[i]:
			break

	return answer