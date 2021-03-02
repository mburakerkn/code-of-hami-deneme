#x = 10 

#if x > 5:
#    raise Exception("X 5'ten büyük olamaz.")
"""
def check_password(psw):
    import re
    if len(psw) < 8 :
        raise Exception("Parola en az 8 olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[_@$]",psw):
        raise Exception("Parola alpha numeric içermelidir.")
    elif re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli parola.")

password = "12345655555aA_"


try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli parola: Else")
finally:
    print("Validation Tamamlandı.")
    """



class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor.")
        else:
            self.name = name



p = Person("Aliaaaa",1989)