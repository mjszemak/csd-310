import msvcrt
from os import system
from pymongo import MongoClient

def main():
    client = MongoClient("mongodb+srv://admin:admin@cluster0.qzqbr2z.mongodb.net/pytech",)

    db = client["mydb"]

    pytech = db["PyTech"]

    records = [
        {
            "student_id": "1007",
            "first_name": "Thorin",
            "last_name": "Oakenshield"
        },
        {
            "student_id": "1008",
            "first_name": "Bilbo",
            "last_name": "Baggins"
        },
        {
            "student_id": "1009",
            "first_name": "Frodo",
            "last_name": "Baggins"
        }
    ]

    output = "Inserted student record %s into the students collection with document_id %s"
    system("cls")
    print('-- INSERT STATEMENTS --')
    for record in records:
        new_student_Id = pytech.insert_one(record).inserted_id
        name = record['first_name'] + ' ' + record['last_name']
        print(output % (name, new_student_Id))
        
    print('\nEnd of program, press any key to exit...')

    while (True):
        if (msvcrt.kbhit()):
            msvcrt.getch()
            break

if __name__ == "__main__":
    main()