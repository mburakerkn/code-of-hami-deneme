"""class Person:
    pass
    

    def __init__(self,name,year):
        self.name = name
        self.year = year
        print("init metodu çalıştı.")

    def intro(self):
        print("Hello There " + self.name)

    def calage(self):
        return 2019 - self.year

p1 = Person("Burak",1999)

p1.intro()
print(f"Adım {p1.intro()}.Yaşım : {p1.calage()}")

"""

class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla()} cevre = {c1.cevre_hesapla()}")
print(f"c2 : alan = {c2.alan_hesapla()} cevre = {c2.cevre_hesapla()}")