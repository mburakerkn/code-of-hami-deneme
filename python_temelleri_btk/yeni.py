# Bankamatik Uygulaması

BurakHesap = {
    'Ad':'Mehmet Burak Erkan',
    'Hesap No':'4543',
    'Bakiye':150,
    'Ek Hesap':8

}

SelmaHesap = {
    "Ad":"Zeynep Selma Erkan",
    "Hesap No":"1700",
    "Bakiye":650,
    "Ek Hesap":200
}

def paracek(hesap,miktar):
    print(f"Merhaba {hesap['Ad']}.")

    if (miktar =< hesap["Bakiye"]):
        print("Paranızı alabilirsiniz.")

    else:
        toplam = hedsp["Bakiye"] + hesap["Ek Hesap"]


        if (toplam >= miktar):
            ehk = input("Ek Hesap Kullanılsın mı ? (E/H)")

            if ehk == "Evet":
                print("Paranızı alabilirsiniz.")

            else:
                print(f"")


paracek(SelmaHesap,10)