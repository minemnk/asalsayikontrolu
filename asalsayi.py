def asal_mi():
    sayi = int(input("Bir sayi giriniz: "))

    if sayi < 2:
        print(f"{sayi} bir asal sayi değildir.")
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                print(f"{sayi} bir asal sayi değildir.")
                break
        else:
            print(f"{sayi} bir asal sayidir.")

asal_mi()
