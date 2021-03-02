"""s1 = int(input("Sayı Girin:"))
s2 = int(input("Sayı Girin:"))

def asalbul(s1,s2):
    for i in range(s1,s2+1):
        if i > 1:
            for x in range(2,i):
                if i % x == 0:
                    break
            else:
                print(i)
                    
                    
asalbul(s1,s2)"""

"""sayi = int(input("Sayı Giriniz:"))

def tamb(x):
    l = []
    for i in range(1,x):
        if x % i == 0:
            l.append(i)
            
    print(l)


tamb(sayi)"""



#def square(num): return num ** 2
numbers = [1,4,7,9,3,6]

r = list(map(lambda n: n**2,numbers))
print(r)

#for item in map(square,numbers):
#    print(item)

