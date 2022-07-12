import msvcrt
from os import system
from pymongo import MongoClient

def main():
    client = MongoClient("mongodb+srv://admin:admin@cluster0.qzqbr2z.mongodb.net/pytech")

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

    record = {"student_id": "1010",
              "first_name": "John",
              "last_name": "Doe"}
    
    output = "Inserted student record into the students collection with document_id %s"
    name = record['first_name'] + ' ' + record['last_name']
    new_student_Id = pytech.insert_one(record).inserted_id
    print('-- INSERT STATEMENTS --')
    print(output % (new_student_Id))
    print('\n')

    doc = pytech.find_one({'student_id' : '1010'})
    print('-- DISPLAYING STUDENT TEST DOC --')
    print("Student ID: %s" % (doc["student_id"]))
    print("First Name: %s" % (doc["first_name"]))
    print("Last Name: %s" % (doc["last_name"]))
    print('\n')

    result = pytech.delete_one({'student_id' : '1010'})

    docs = pytech.find()

    print('-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --')
    for doc in docs:
        print("Student ID: %s" % (doc["student_id"]))
        print("First Name: %s" % (doc["first_name"]))
        print("Last Name: %s" % (doc["last_name"]))
        print('\n')

    print('\nEnd of program, press any key to exit...')

    while (True):
        if msvcrt.kbhit():
            msvcrt.getch()
            break
    


if __name__ == "__main__":
    main()














        
