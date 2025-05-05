class Human:

    life = True

    def __init__(self, name="", age=0, gender=0):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age: int):
        self.__age = age

    def getAge(self):
        return self.__age

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender


class Student(Human):

    def __init__(self, name="", age=0, gender=0):
        super().__init__(name, age, gender)  # передаем параметры в родительский класс
        self.__classes = ""
        self.location = "outside"

    def setClasses(self, classes):
        self.__classes = classes

    def getClasses(self):
        return self.__classes


class Autobus:

    location: str
    places = 10

    def __init__(self, passagers: list):
        self.passagers = passagers

    def takPassagers(self, passagers: list, child: Student):
        child.location = "inside"
        Autobus.places -= len(passagers)
        print(Autobus.places, child.location)


student1 = Student(name="Рафик", age=20, gender=1)  # передаем параметры при создании объекта
student2 = Student(name="Иван", age=22, gender=1)
student3 = Student(name="Мария", age=18, gender=2)

print(student1.getName())  # Выводим имя студента

bus = Autobus(passagers=[student2, student3, student1])
bus.takPassagers(bus.passagers, student1)  # Добавляем пассажиров в автобус
