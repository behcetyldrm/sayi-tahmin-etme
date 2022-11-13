from random import randint

tutulanSayi = randint(0,100)
n = 0 #Tahmin etme sayısı

print("******SAYI TAHMİN ETMECE****** \n")
while True:
    
    try:
        tahmin = int(input("Sayı Tahmininiz: "))
        n += 1

        if tahmin == tutulanSayi:
            print(f"Tebrikler sayıyı buldun! \nTutulan sayı: {tutulanSayi} \nToplam tahmin sayınız: {n}")
            
            devam = input("Tekrar oynamak ister misin? (e/h): ") # e -> oyna h -> bitir
            if devam == "e":
                n = 0
                tutulanSayi = randint(0,100)
                continue
            elif devam == "h":
                print("Hoşçakal...")
                break
            else:
                print("Farklı bir değer girildiğinden oyun bitiriliyor")
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

    

