class Human:

    life = True

    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__gender = 0

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self,age:int):
        self.__age = age
    def getAge(self):
        return self.__age

    def setGender(self,gender):
        self.__gender = gender
    def getGender(self):
        return self.__gender

class Student(Human):

    def __init__(self):
        super().__init__()
        self.__classes = ""
        self.location = "outside"

    def setClasses(self,classes):
        self.__classes = classes
    def getClasses(self):
        return self.__classes

class Autobus:

    location : str
    places = 10

    def __init__(self,passagers :list):
        self.passagers = passagers

    def takPassagers(self,passagers:list,child:Student):
        child.location = "inside"
        Autobus.places -= len(passagers)
        print(f"{Autobus.places} + {str(child.location)}")
    def quitPassagers(self,passagers:list,child:Student):
        child.location = "изганг"
        Autobus.places += len(passagers)
        print(f"{Autobus.places} + {str(child.location)}")

student1 = Student()
student2 = Student()
student3 = Student()
student1.setName("рафик")
print(student1.getName())

print(student1.location)







