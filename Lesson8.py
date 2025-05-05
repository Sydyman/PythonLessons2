class Human:
    __name : str
    __location: str

    def __init__(self,name = "сасун"):
        self.__name = name
        self.__location = "Москвабад"

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__name + ":" + self.__location

    def setLocation(self,location):
        self.__location = location

class Child(Human):
    __age = 6

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age


chel = Human()
print(chel.getLocation())

patsan = Child()
patsan.setLocation("садик")
patsan.setName("Владик")
print(patsan.getName())
print(patsan.getAge())

