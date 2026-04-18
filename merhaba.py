def asal_sayi_mi(x): 
    for i in range(2, int(x**0.5) + 1): 
        if x % i == 0:
            break
    else:
        print("asaldir")
asal_sayi_mi(13)
