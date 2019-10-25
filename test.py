class Employee:
    __id = ""
    __name = ""
    __position = ""
    __salary = 0

    def __init__(self,id,name,position,salary):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salary = salary

    def getid(self):
        return self.__id
    def getname(self):
        return self.__name
    def getposition(self):
        return self.__position
    def getsalary(self):
        return self.__salary

class Main():
    allstaff = []
    allofficer = []
    allmanager = []
    staffno = 0

    def addstaff(self,id,name,position,salary):
        self.allstaff.append(Employee(id,name,position,salary))
        self.staffno += 1
    def addofficer(self,id,name,position,salary):
        self.allofficer.append(Employee(id,name,position,salary))
        self.staffno += 1
    def addmanager(self,id,name,position,salary):
        self.allmanager.append(Employee(id,name,position,salary))
        self.staffno += 1
    def deletestaff(self):
        for i in range(len(self.stafflist)):
            if id == self.allstaff[i].getid():
                return False
        return True
    def checkID(self, id):
        bool = True
        for i in range(len(self.allstaff)):
            if(id == self.allstaff[i].getid()):
                bool = False
        return bool
    def viewdata(self):
        staffsalary = []
        officersalary = []
        managersalary = []
        staffsalarytotal = 0
        officersalarytotal = 0
        managersalarytotal = 0
        for i in range(len(self.fullstaff)):
            if len(self.fullstaff) == 0:
                pass
            staffsalary.append(self.fullstaf[i].getsalary())
        for i in range(len(self.fullofficer)):
            if len(self.fullofficer) == 0:
                pass
            officersalary.append(self.fullofficer[i].getsalary())
        for i in range(len(self.fullmanager)):
            if len(self.fullmanager) == 0:
                pass
            managersalary.append(self.fullmanager[i].getsalary())
        for i in range(len(staffsalary)):
            if (len(staffsalary) == 0):
                pass
            staffsalarytotal += int(staffsalary[i])
        for i in ragne(len(officersalary)):
            if len(officersalary) == 0:
                pass
            officersalarytotal += int(officersalary[i])
        for i in range(len(managersalary)):
            if (len(managersalary)) == 0:
                pass
            managersalarytotal += int(managersalary[i])

        if len(staffsalary) != 0:
            staffmean = staffsalarytotal / len(staffsalary)
            print("Staff")
            print("Minimum Salary: " + str(min(staffsalary)))
            print("Maximum Salary: " + str(max(staffsalary)))
            print("Average Salary: " + str(staffmean))
        if len(officersalary) != 0:
            officermean = officersalarytotal / len(officersalary)
            print("Officer")
            print("Minimum Salary: " + str(min(officersalary)))
            print("Maximum Salary: " + str(max(officersalary)))
            print("Average Salary: " + str(officermean))
        if len(managersalary) != 0:
            managermean = managersalarytotal / len(managersalary)
            print("Manager")
            print("Minimum Salary: " + str(min(managersalary)))
            print("Maximum Salary: " + str(max(managersalary)))
            print("Average Salary: " + str(managermean))
        if (len(staffsalary) == 0) and (len(officersalary) == 0) and (len(managersalary) == 0):
            print("Data Unavailable")

main = Main()

while True:
    print("\n1. New Staff\n2. Delete Staff\n3. View Summary Data\n4. Save & Exit")
    choice = input("Input Choice: ")
    if choice == "1":
        flag = False
        while True:
            if flag == True:
                break
            ID = input("ID: ")
            if (len(ID) == 5) and (ID[0] == "S" or "s") and (ID[1:5].isdigit()):
                if main.checkID(ID) == True:
                    while True:
                        if flag == True:
                            break
                        name = input("Name: ")
                        if (len(name) <= 20):
                            while True:
                                if flag == True:
                                    break
                                position = input("Position: ")
                                if position == "staff" or position == "officer" or position == "manager":
                                    while True:
                                        salary = input("Salary: ")
                                        if flag == True:
                                            break
                                        if position == "staff":
                                            if int(salary) >= 3500000 and int(salary) <= 7000000:
                                                main.addstaff(id,name,position,salary)
                                                print("Data Added")
                                                flag = True
                                                break
                                            else:
                                                print("Invalid")
                                        elif position == "officer":
                                            if int(salary) >= 7000001 and int(salary) <= 10000000:
                                                main.addofficer(id,name,position,salary)
                                                print("Data Added")
                                                flag = True
                                                break
                                            else:
                                                print("Invalid")
                                        elif position == "manager":
                                            if int(salary) > 10000000:
                                                main.addmanager(id,name,position,salary)
                                                print("Data Added")
                                                flag = True
                                                break
                                            else:
                                                print("Invalid")
                                else:
                                    print("Invalid")
                        else:
                            print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")

    elif choice == "2":
        main.deletestaff()
    elif choice == "3":
        main.viewdata()
