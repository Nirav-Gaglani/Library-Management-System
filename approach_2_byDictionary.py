dictLib={}
stList={}
with open("stock.txt", "r") as f:
    text = f.read().splitlines()
for item in text:
    line = item.split(':')
    dictLib[line[0]] = int(line[1])

with open("st_data.txt", "r") as f:
    text = f.read()
    if text != "":
        text = text.splitlines()
        for item in text:
            line = item.split(': ')
            stList[int(line[0])] = line[1]

class Library:
    global dictLib
    global stList
    def updateStock(self):
        password = input("Enter password: ")
        # Enter "123!@#" as password to update the library stock
        if password == "123!@#":
            while True:
                bookName = input("Enter book name: ")
                qty = int(input(f"Enter quantity of {bookName}: "))
                if bookName not in dictLib.keys():
                    dictLib[bookName] = [qty]
                else:
                    dictLib[bookName]+=1
                gate = int(input(("Enter any integer to further update OR enter -9 to exit: ")))
                if gate==-9:
                    break
        else:
            print("Incorrect Password.")
    def issueBook(self, bookName, eCode):
        if bookName not in dictLib.keys():
            print(f"{bookName} book is not available in Library!")
        else:
            if dictLib[bookName] == 0:
                    print(f"{bookName} is out of Stock, Kindly wait till it is returned.")
            else:
                if eCode in stList.keys():
                    print("One book is already isuued to You. Another can't be isuued till the 1st is returned.")
                else:
                    print(f"{bookName} book Isuued to code number {eCode}")
                    dictLib[bookName]-=1
                    stList[eCode] = bookName
    def returnBook(self, bookName, eCode):
        if bookName not in dictLib.keys():
            print("Thank You for your valuable contribution to the Library")
            dictLib[bookName] = 1
        else:
            dictLib[bookName]+=1
            try:
                del stList[eCode]
            except ValueError:
                pass
        print(f"{bookName} book received from code number {eCode}")
    def availableBooks(self):
        for key in dictLib.keys():
            print(f"{key}: {dictLib[key]}\n")
    def stDataBase(self):
        for key in stList.keys():
            print(f"{key}: {stList[key]}\n")

class Student:
    def __init__(self):
        self.eCode = int(input("Enter your library code: "))
    def getCode(self):
        return self.eCode
    def isuueBook(self):
        self.book = input("Enter name of book you want to Isuue: ")
        return self.book
    def returnBook(self):
        self.book = input("Enter name of book you want to Return: ")
        return self.book
library = Library()
msg = input("Enter Anything to enter Library: ")
# Type "id!@#" to update stock
if msg == "id!@#":
    library.updateStock()
student = Student()
while True:
    try: 
        print('''Welcome to Library
        Enter 99 to see list of available books
        Enter 1 to Isuue a Book
        Enter 2 to Return a Book
        Enter 3 to Exit from Library''')
        num = int(input("Enter your choice here: "))
        if num == 99:
            library.availableBooks()
        elif num == 1:
            library.issueBook(student.isuueBook(), student.getCode())
        elif num == 2:
            library.returnBook(student.returnBook(), student.getCode())
        elif num == 3:
            with open("stock.txt", "w") as f:
                for key in dictLib.keys():
                    f.write(f"{key}: {dictLib[key]}\n")
            with open("st_data.txt", "w") as f:
                for key in stList.keys():
                    f.write(f"{key}: {stList[key]}\n")
            exit()
        else: 
            print("Plese Enter a Valid Choice")
    except ValueError:
        print("Please enter 1 2 3 or 9")
    except Exception as e:
        print(e)