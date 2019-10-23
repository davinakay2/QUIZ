class Employee:
    __id = 0
    __name = ""
    __position = ""
    __salary = 0

    def setdata(self,id,name,position,salary):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salary = salary

    def showdata(self):
        print("ID\t\t:",self.__id)
        print("Name\t:",self.__name)
        print("Position:",self.__position)
        print("Salary\t:",self.__salary)

def main():
    emp = Employee()
    emp.setdata(1,"davina","CEO",1)
    emp.showdata()

if __name__ == '__main__':
    main()

with open("salary.txt","w") as output:
    output.write()