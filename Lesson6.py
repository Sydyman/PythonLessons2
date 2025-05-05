class Human:

    def __init__(self,name,age,mast,srok):
        self.name = name
        self.age = age
        self.mast = mast
        self.srok = srok

    def otsidka(self):
        if self.mast == "ВОР":
            self.srok -= self.srok
        print(f"{self.name} на волю через {self.srok}")



    def raskidat(self):
        print(f"Этого пендалая зовут { self.name } ему {self.age} лет и его масть {self.mast} и ему осталось сидеть {self.srok}")


patsan1 = Human("вася",10,"шнырь",1)
patsan2 = Human("петя",35,"домушник",2)
pahan = Human("Смолян",40,"ВОР",30)
pahan.raskidat()
pahan.otsidka()


class Patsan(Human):


    def __init__(self,name,age,mast,srok,ne_pidor):
        super().__init__(name,age,mast,srok)
        self.ne_pidor = ne_pidor

    def uznat(self):
        if self.ne_pidor:
            print("этот додик не петух")
        else:
            print("петушара")
    def raskidat(self):
        print(f"все нормальные {str(self.name)}")

patsan3 = Patsan("гриша",21,"чухан",33,False)
patsan4 = Patsan("Арестант",23,"ВОР",32,True)
patsan3.raskidat()
patsan3.otsidka()
patsan3.uznat()
patsan4.raskidat()
patsan4.otsidka()
patsan4.uznat()

patsan4.raskidat()

class Zona():
    rejim = "Строгий"


    def __init__(self,zeki:list,zek:Human, camera=0):
        self.zeki = zeki
        self.camera = camera
        self.zek = zek


    def ktoSidit(self):
        print(f"в это зоне сидят эти зеки ")
        for zek in self.zeki:
            print(f" {zek.name}")

    def gdeSidit(self,zek:Human):
        self.camera += 1
        self.zek = zek
        print(f"{self.zek.name} зек сидит в этой камере {self.camera}")


belyi_delfin = Zona(zeki = [pahan,patsan1,patsan2,patsan3,patsan4],zek= pahan)

belyi_delfin.gdeSidit(pahan)
belyi_delfin.gdeSidit(patsan1)

belyi_delfin.ktoSidit()



















