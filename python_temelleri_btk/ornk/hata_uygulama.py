liste = ["1","2","3","svb","5i"]

"""for i in liste:
    try:
        r = int(i)
        print(r)
    except ValueError:
        continue
"""



while True:
    s = input("Sayı Giriniz:")
    print(type(s))
    if type(s) == type(int):
        print("Doğru girdiniz.")
    elif (s == "q") or (s == "Q"):
        print("Tekrar giriniz.")
    else:
        raise Exception("Yanlış değer.")

