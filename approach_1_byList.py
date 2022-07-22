l = []
qt = []
stList = []

with open("stock.txt", "r") as f:
    text = f.read()
    text = text.splitlines()
for item in text:
    line = item.split(':')
    l.append(line[0])
    qt.append(int(line[1]))

with open("st_data.txt", "r") as f:
    text = f.read()
    if text != "":
        text = text.splitlines()
        for item in text:
            stList.append(int(item))

class Library:
    global l
    global qt
    global stList
    def updateStock(self):
        password = input("Enter password: ")
        # Use password as "123!@#" to enter books in the stock text file 
        if password == "123!@#":
            while True:
                bookName = input("Enter book name: ")
                qty = int(input(f"Enter quantity of {bookName}: "))
                if l.count(bookName)==0:
                    l.append(bookName)
                    qt.append(qty)
                else:
                    for i, item in enumerate(l):
                        if item == bookName:
                            qt[i]+=1
                gate = int(input(("Enter any integer to further updat OR enter -9 to exit: ")))
                if gate==-9:
                    break
        else:
            print("Incorrect Password.")
    def issueBook(self, bookName, eCode):
        if (l.count(bookName)==0):
            print(f"{bookName} book is not available in Library!")
        else:
            for i, item in enumerate(l):
                if item==bookName:
                    if qt[i] == 0:
                        print(f"{item} is out of Stock, Kindly wait till it is returned.")
                    else:
                        print(f"{bookName} book Isuued to code number {eCode}")
                        qt[i]-=1
                        stList.append(eCode)
    def returnBook(self, bookName, eCode):
        if(l.count(bookName)==0):
            print("Thank You for your valuable contribution to the Library")
            l.append(bookName)
            qt.append(1)
        else:
            for i, item in enumerate(l):
                if item == bookName:
                    qt[i]+=1
                try:
                    stList.remove(eCode)
                except ValueError:
                    pass
        print(f"{bookName} book received from code number {eCode}")
    def availableBooks(self):
        for i, item in enumerate(l):
            print(i+1, item, qt[i])
    def stDataBase(self):
        print(stList)

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
msg = input("Enter \"Hello\" to enter Library: ")
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
                for i, item in enumerate(l):
                    f.write(f"{item}: {qt[i]}\n")
            with open("st_data.txt", "w") as f:
                for item in stList:
                    f.write(f"{str(item)}\n")
            exit()
        else: 
            print("Plese Enter a Valid Choice")
    except ValueError:
        print("Please enter 1 2 3 or 99")
    except Exception as e:
        print(e)