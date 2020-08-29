class Library:
    def __init__(self,listofbook,name):
        self.listofbooks=listofbook
        self.name=name
        self.booklenddata={}

        for book in self.listofbooks:
            self.booklenddata[book]=None

    def display(self):
        print("***BOOKS ARE***")
        for index,book in enumerate(self.listofbooks):
            print(f"{index}.{book}")

    def lendbook(self,lendername,book):
        if book in self.listofbooks:
            if self.booklenddata[book] is None:
                self.booklenddata[book]=lendername
            else:
                print(f"Sorry these book is lend by {self.booklenddata[book]}")
        else:
            print(f"You Written wrong Book Name")

    def addbook(self,newbook):
        if newbook not in self.listofbooks:
            self.listofbooks.append(newbook)
            self.booklenddata[newbook]=None
            print("Successfully Added Book in Library")
        else:
            print("These Book already in Library")

    def deletebook(self,book):
        self.listofbooks.remove(book)
        self.booklenddata.pop(book)

    def returnbook(self,book):
        print(f"Book is return by {self.booklenddata[book]}")
        if book in self.listofbooks:
            self.booklenddata[book]==None
        else:
            print("Sorry but this book is not Lend")

Ajinkya=Library(["Alchemist","Rich Dad and Poor Dad","Sherlock Homes","One minute Mananger","Rich and Knight for Artifficial Inteligent"],"Ajinkya ")

def main():
    print("A simple Library Management class made in python and made by Ajinkya Makode")
    print("Welcome to Library, We have currently these books...")
    Exit=False
    while Exit is not True:
        print(f"\nWhat operation you want to perform? : \n1 for \"Lend\" \n2 for \"Add book\" \n3 for \"Delete Book\" \n4 for \"Display\" \n5 for \"Return Book\" \n6 for \"Exit\"")
        userinput=input("\nProvide Input: ")
        if userinput=="1":
            Ajinkya.display()
            lendername=input("Enter Your Name: ")
            book=input("Enter Book Name: ")
            Ajinkya.lendbook(lendername,book)

        elif userinput=="2":
            newbook=input("Enter Newbook Name: ")
            Ajinkya.addbook(newbook)

        elif userinput=="3":
            Ajinkya.display()
            book=input("Which Book do you want to Delete: ")
            Ajinkya.deletebook(book)

        elif userinput=="4":
            Ajinkya.display()

        elif userinput=="5":
            book=input("Enter which book do you want to return: ")
            Ajinkya.returnbook(book)

        elif userinput=="6":
            Exit=True

        else:
            print("Please enter 1/2/3/4/5/6 only")
if __name__ == '__main__':
    main()