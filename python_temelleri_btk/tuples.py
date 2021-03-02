ogrenciler = {}

number = input("Öğrenci No:")
name = input("Öğrenci Adı:")
surname = input("Öğrenci Soyadı:")
phone = input("Öğrenci Tel. :")

"""ogrenciler[number] = {
    "ad": name,
    "soyad": surname,
    "telefon": phone
}"""
ogrenciler.update({
    number: {
       "ad": name,
       "soyad": surname,
       "tel": phone
    }
})

ogrNO = input("No Giriniz:")
ogrenci = ogrenciler[ogrNO]
print(ogrenciler)