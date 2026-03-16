import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/Users/atharvkankal/PycharmProjects/FaceRecognitionAttendanceSystem/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognitionattendanc-8ab95-default-rtdb.firebaseio.com/"
})

ref  = db.reference("Students")
data = {
    '3062':
        {
            "Name": "Atharv Kankal",
            "Branch": "Engineering",
            "Year": "Third",
            "Roll":62,
            "total_attendance":0,
            "standing":"AIDS",
            "Last_attendance_time": "2023-11-22 00:54:34",
            "Starting_year" :  2021

        },
    '3074':
        {
            "Name": "Chetana Koli",
            "Branch": "Engineering",
            "Year": "Third",
            "Roll": 74,
            "total_attendance": 0,
            "standing": "AIDS",
            "Last_attendance_time": "2023-11-22 00:54:34",
            "Starting_year": 2022
        },
    '3038':
        {
            "Name": "Divya",
            "Branch": "Engineering",
            "Year": "Third",
            "Roll": 38,
            "total_attendance": 0,
            "standing": "AIDS",
            "Last_attendance_time": "2023-11-22 00:54:34",
            "Starting_year": 2022
        },
    '001':
        {
            "Name": "Appa",
            "Branch": "Engineering",
            "Year": "Third",
            "Roll":1,
            "total_attendance":1,
            "standing":"AIDS",
            "Last_attendance_time": "2024-01-16 16:28:34",
            "Starting_year" :  2021

        },
     '3037':
        {
            "Name": "Rushi",
            "Branch": "Engineering",
            "Year": "Third",
            "Roll":37,
            "total_attendance":0,
            "standing":"AIDS",
            "Last_attendance_time": "2023-11-22 00:54:34",
            "Starting_year" :  2021

        },
}

for key,value in data.items():
    ref.child(key).set(value)
