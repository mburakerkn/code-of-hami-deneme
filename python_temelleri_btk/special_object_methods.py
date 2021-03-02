"""mylist = [1,5,8,9,2]
mystr = "My String"
print(len(mylist))
print(len(mystr))"""


class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")

    def __del__(self):
        print("Movie deleted.")
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

m = Movie("Film Adı","Yönetmen Adı",120)

print(len(m))



print(m)

del m
print(m)