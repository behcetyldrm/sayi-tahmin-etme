from random import randint

tutulanSayi = randint(0,100)
n = 0

print("******SAYI TAHMİN ETMECE****** \n")
while True:
    
    try:
        tahmin = int(input("Sayı Tahmininiz: "))
        n += 1

        if tahmin == tutulanSayi:
            print(f"Tebrikler sayıyı buldun! \nTutulan sayı: {tutulanSayi} \nToplam tahmin sayınız: {n}")
            break
        else:
            print("Tekrar deneyin!")
            if tahmin > tutulanSayi:
                print(f"İPUCU: {tahmin}'den daha küçük bir sayı giriniz")
            elif tahmin > 100:
                print("100'den daha küçük sayılar giriniz")
            else:
                print(f"İPUCU: {tahmin}'den daha büyük bir sayı giriniz")
        
    except:
        print("Lütfen sayı giriniz!")

    

