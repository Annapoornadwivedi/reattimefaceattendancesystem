import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-40a9a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "111":
        {
            "name": "Annapoorna Dwivedi",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "year": 3,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "222":
        {
            "name": "Puja Ukey",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 12,
            "year": 3,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "333":
        {
            "name": "Mamta Panda",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "year": 3,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
"444":
        {
            "name": "Laxmi Tripathi",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 8,
            "year": 3,
            "last_attendance_time": "2023-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
