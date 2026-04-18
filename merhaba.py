def asal_sayi_mi(x): 
    for i in range(2, int(x**0.5) + 1): 
        if x % i == 0:
            print("asal degildir")
            break
    else:
        print("asaldir")
def asal_ayikla(x):
    if x == 2: "print asaldir."
    if x % 2 != 0: asal_sayi_mi(x)
asal_ayikla(4)