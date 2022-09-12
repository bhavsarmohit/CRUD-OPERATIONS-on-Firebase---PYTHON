from firebase import firebase

firebase = firebase.FirebaseApplication("https://--------------.firebaseio.com/",None) #Link of Realtime Database



# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
user = auth.sign_in_with_email_and_password(email, password)



# Get a reference to the database service
db = firebase.database()
db.child("Database1")

user = db.child("stud_info").get()
print(user.value())



# post send to firebase
data={
    'Name':'Mohit Bhavsar',
    'Email':'masfd@id',
    'Phone':918084
}
result = firebase.post('Database1/stud_info/',data)
print(result)
