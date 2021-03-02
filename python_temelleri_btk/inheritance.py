class Person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print("Person Created.")


    def eat(self):
        print("I am eating.")

    def who_am_i(self):
        print("I am a person.")
class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print("Student Created.")
    
    def sayHello(self):
        print("Hello I am a student.")
    def who_am_i(self):
        print("I am a student.")
class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher.")
        
p1 = Person("Ali","Yılmaz")
s1 = Student("Çınar","Turan","881")
t1 = Teacher("Serkan","Yılmaz","Math")

t1.who_am_i()
print(p1.fname + " " + p1.lname)
print(s1.fname + " " + s1.lname + " " + s1.studentNumber)

p1.who_am_i()
s1.who_am_i()
s1.eat()
s1.sayHello()