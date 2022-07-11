import msvcrt
from os import system
from pymongo import MongoClient

def main():
    url = "mongodb+srv://admin:admin@cluster0.qzqbr2z.mongodb.net/pytech";
    client = MongoClient(url)
    db = client.pytech

    system('cls')
    print('-- Pytech Collections List --')
    print(db.list_collection_names())
    print('\nEnd of program, press any key to exit...')

    while (True):
        if msvcrt.kbhit():
            msvcrt.getch()
            break
    

if __name__ == "__main__":
    main()