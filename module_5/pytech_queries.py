import msvcrt
from os import system
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@cluster0.qzqbr2z.mongodb.net/pytech",)

db = client["mydb"]

pytech = db["PyTech"]

docs = pytech.find()

system('cls')

print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')
for doc in docs:
    print("Student ID: %s" % (doc["student_id"]))
    print("First Name: %s" % (doc["first_name"]))
    print("Last Name: %s" % (doc["last_name"]))
    print('\n')
    

print('-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --')
doc = pytech.find_one({"student_id" : "1007"})
print("Student ID: %s" % (doc["student_id"]))
print("First Name: %s" % (doc["first_name"]))
print("Last Name: %s" % (doc["last_name"]))
print('\n')

print('\nEnd of program, press any key to exit...')

while (True):
	if msvcrt.kbhit():
		msvcrt.getch()
		break