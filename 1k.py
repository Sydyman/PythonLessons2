import random


class Zek:
    name = "валера"
    srok = 8

    def getName():
        print(Zek.name)

Zek.getName()



Zek.mast = "мужик"

print(Zek.mast)

setattr(Zek, 'block',1.5)

print(Zek.block)


class Ment:

    def __init__(self,name : str , age : int):
        self.name = name
        self.age = age


ment = Ment("валера",23)

print(ment.__dict__)
print("------------------------------")

class Fabrique:
    oil = 500

    def __init__(self,name,rashod):
        self.name = name
        self.rashod = rashod
        self.location = random.choice(["германия","австрия","чехия"])

    def StartCar(self):
        Fabrique.oil -= self.rashod
        print(f"{self.name} машина поехала и израсходовала топлива равного = {self.rashod} топлива осталось {Fabrique.oil }")
        print(f"тачка находится {self.location}")


bmw = Fabrique("bmw",25)
bmw.StartCar()

print(Fabrique.oil)


class mercFabrique(Fabrique):
    def __init__(self,name,rashod,litrov,hp):
        super().__init__(name,rashod)
        self.litrov = litrov
        self.hp = hp

    def power(self):

        if self.litrov > 3:
            self.hp = 300
        else:
            self.hp

        print(f"лощадинные силы равны {self.hp}")

e500 = mercFabrique("волчок",30,5,200)
e500.power()
e500.StartCar()

print("-------------------------")

class Human:
    alive = True

    def __init__(self,name):
        self.name = name
        self.gender = random.choice(["мужчина","женщина"])
        self.age = random.randint(0,100)

    def checkLive(self):
        if self.age > 90 :
            Human.alive = False
            if Human.alive != True:
                return "мертв сука"
        else:
            return f"{self.name} живее всех живыхх"

chel = Human("вася")
print(chel.name,chel.gender,chel.age)
print(chel.checkLive())

print("---------------------------")

class Child(Human):
    slocation : str

    def __init__(self,name,location):
        super().__init__(name)
        self.location = location



class Autobus:

    sits = 25




    def takeKids(self,group: list()):
        self.group = group

        Autobus.sits -= len(group)

        return f"в автобусе сидят {self.group} мест осталось {Autobus.sits}"




malchik = Child("ванька","москва")
malchik1 = Child("колька","москва")
malchik2 = Child("сыдька","химки")
malchik3 = Child("додочь","кизилюрт маленькая сицилия")
malchik4 = Child("анька","москва")
malchik5 = Child("санька","москва")
print(malchik1.checkLive())

bus = Autobus()

bus.takeKids([malchik.name,malchik2.name,malchik3.name,malchik4.name])


bus.__str__()

print("---------------------")

class Entity:

    _prototype : str
    _location: str

    def __init__(self,name = "experimental"):
        self._prototype = name
        self._location = "Cyber"

    def get_name(self):
        return  self._prototype

    def get_location(self):
        return self._prototype + " : " + self._location

    def set_location(self,location):
        self._location = location


ent = Entity()
print(ent.get_location())

class Mob(Entity):

    _stage = 7
    
    def __init__(self, name = "Mercy",):
        super().__init__(name)
        self._name = name

    
    def set_age(self,age):
        self._stage = age

    def get_age(self):
        return self._name + ":" +  str(self._stage)
        

mob = Mob()
mob.set_location("boston")
print(mob.get_location())
print(mob.get_location())
print(mob.get_age())
print("--------------------")

class Bus:
    __passageers : list()

    def __init__(self,passageers : list):
        self.__passageers = passageers

    def take_childs(self,passagers:list):
        self.__passageers = self.__passageers + passagers

    def throw_cjilds(self,passageers:list ):
        for mob in passageers:
            if mob in self.__passageers:
                self.__passageers.remove(mob)


    def prin_location(self):
        for mob in self.__passageers:
           print(mob.get_location())

    def setLocForChild(self,newLoc):
        for mob in self.__passageers:
            mob.set_location(newLoc)

mob1 = Mob("fear")
mob2 = Mob("fearless")
mob3 = Mob("Unfear")
mob4 = Mob("superfear")


bus = Bus([mob1,mob2,mob3,mob4])
bus.prin_location()
bus.take_childs([mob])
bus.prin_location()
print("-------------------------")
bus.throw_cjilds([mob1])
bus.prin_location()

bus.setLocForChild("Сербия")

bus.prin_location()



print("запоминай дура \n-----------------------------------")




list1 = [ 1,1,1,3,32,32, "hello"]

def delee(loc_list:list):
    pus_list = list()
    for i in loc_list:
        try:
            pus_list.append(i / 2)
        except Exception as oshibka:
            print(oshibka)
        finally:
            print(i)
    return pus_list

print(delee(list1))

print("парктика класофф \n"
      "---------------------------------------")


class Humanoid:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def getName(self) :
        return f"Солдата зовут {str(self.__name)}"

    def setName(self,name):
        self.__name = name

    def getAge(self):
        return f"возраст {self.__age}"

    def setAge(self,age):
        self.__age = age

soldier = Humanoid("альфредо",22)

class Rota:

    __soldiers : list

    def __init__(self,numeration):
        self.numeration = numeration
        self.__soldiers = list()

    def take_members(self,soldiers:list):
        self.__soldiers = self.__soldiers + soldiers



    def getSoldiers(self):
        print(f" Номер {self.numeration}  Личный состав Роты:")
        for soldier in self.__soldiers:
         print(  soldier.getName() )









print(soldier.getName())
print(soldier.getAge())


rota1 = Rota("9 рота")
soldat = Humanoid("Алекс",33)
soldat2 = Humanoid("Алексf",333)
rota1.take_members([soldat])
rota1.take_members([soldat2])
rota1.take_members([soldier])



print("-----------------------------------------")
rota1.getSoldiers()

print("ММО RPG \n"
      "----------------------------------------------")

class Fighter:

    def __init__(self,name,damage,health):
        self.name = name
        self.damage = damage
        self.health = health

    def attackuation(self, enemy:"Fighter"):
        print(f"{self.name} ударил {enemy.name}{enemy.health} с мощью {self.damage}  ")
        enemy.health -= self.damage
        print(f"осталось здоровья {enemy.health}")

    def is_alive(self) -> bool:
        return self.health > 0

    def __str__(self) -> str:
        return f"{self.name}  осталось {self.health} "



##


class Wrestler(Fighter):
    pass

class Striker(Fighter):
    pass



boets1 = Wrestler("Ислам Нюхачев",76,399)

boets2 = Striker("Нотариус МакКрекер",100,300)

def mma(boyka1:Fighter,boyka2:Fighter):
    while boyka1.is_alive() and boyka2.is_alive():
        boyka1.attackuation(boyka2)
        if boyka2.is_alive():
            boyka2.attackuation(boyka1)




    print(f"{boyka1}, жив {boyka1.health}")
    print(f"{boyka2}, жив {boyka2.health}")

mma(boets1,boets2)
































