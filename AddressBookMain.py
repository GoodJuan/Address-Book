class Human:
    name = ""
    phonenumber = 0
    iD = ""
    def __init__(self, na, num, i):
        self.name = na
        self.phonenumber = num
        self.iD = i

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phonenumber

    def getiD(self):
        return self.iD

    def getPersonTraits(self):
        output = "\n\nYour person's name is: " + self.name + "\nYour person's phone number is: " + self.phonenumber + "\nYour person's iD number is: " + self.iD +"\n\n"

        return output

addressBook = []

while True:
    searchOrAdd = input("\n\nHello. Would you like to search or add an address.\nPlease enter:\n"
                        "1) To search\n"
                        "2) To add.\n"
                        "3) To exit.")


    #search
    if searchOrAdd == 1 and len(addressBook) > 0:
        found = False
        scanType1 = input("\nWhat would you like to search for today?\nPlease input:\n"
                         "1) Name\n"
                         "2) Phonenumber\n"
                         "3) iD")
        if scanType1 == 1:
            inName = raw_input("Please input your person's name: ")

            for x in range(0, len(addressBook)):
                if addressBook[x].getName() == inName:
                    print(addressBook[x].getPersonTraits())
                    found = True
                    break

        elif scanType1 == 2:
            inNum = raw_input("Please input your person's number: ")

            for x in range(0, len(addressBook)):
                if addressBook[x].getPhone() == inNum:
                    print(addressBook[x].getPersonTraits())
                    found = True
                    break

        elif scanType1 == 3:
            inID = raw_input("Please input your person's iD: ")

            for x in range(0, len(addressBook)):
                if addressBook[x].getiD() == inID:
                    print(addressBook[x].getPersonTraits())
                    found = True
                    break

        if (not found):
            print("Your person was not found. Please try again.")

    #add
    elif searchOrAdd == 2:
        nam = raw_input("\nPlease input your name: ")
        number = raw_input("\nPlease input your phonenumber: ")
        iD = raw_input("\nPlease input your iD: ")
        addressBook.append(Human(nam, number, iD))



    elif searchOrAdd == 3:
        print("Bye!")
        break

    else:
        print("Wrong input or book is empty. Please try again.")

