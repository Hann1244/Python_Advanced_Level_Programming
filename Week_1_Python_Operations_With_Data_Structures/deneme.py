#Kullanıcıdan alınan sayının bütün tam bölenlerini bir liste olarak yazan fonk 
#En az 3 basamaklı bir sayı olsun


'''def tam_bolenler(sayi):
    if not isinstance(sayi, int):
        print("Lütfen geçerli bir tam sayı girin.")
    if sayi < 100:
        print("Lütfen en az üç basamaklı bir sayı girin.")
    
    bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
    return bolenler

try:
    sayi = input("En az üç basamaklı bir sayı girin: ")
    if not sayi.isdigit():
        print("Lütfen sayı giriniz")
    else:
        sayi = int(sayi)
        print("Tam bölenler:", tam_bolenler(sayi))
except Exception as e:
    print("Hata:", e)'''



'''sayi = input("LÜtfen bir sayı giriniz")
try:
    if sayi.lstrip('-').isdigit():# girilen sayının tamsayı olup olmadığını kontrol ediyoruz.
        my_num= int(sayi)# girilen değeri int tipine dönüştürdük
        if my_num>100:
            bolenler = []
            sayac = 0
            for i in range(1,my_num):
                if my_num%i==0:
                    sayac = sayac + 1
                    #sayac+=1
                    bolenler.append(i)
            print(f"{sayi} sayısının {sayac} adet böleni bulundu")        
            for sayilar in bolenler:
                print(sayilar)

        else:
            print("Lütfen 100'den büyük bir tamsayı giriniz")
except Exception as e:
    print(f"Hata = {e}")'''



'''def tam_bolenler(sayi):
    if not isinstance(sayi, int):
        raise ValueError("Lütfen geçerli bir tam sayı girin.")
    if sayi < 100:
        raise ValueError("Lütfen en az üç basamaklı bir sayı girin.")
    
    bolenler = [i for i in range(1, sayi + 1) if sayi % i == 0]
    return bolenler

while True:
    try:
        sayi = input("En az üç basamaklı bir sayı girin: ")
        if not sayi.isdigit():
            print("Lütfen sayı giriniz")
            continue
        sayi = int(sayi)
        print("Tam bölenler:", tam_bolenler(sayi))
    except ValueError as e:
        print("Hata:", e)
'''

#Dışarıdan girilen string tipindeki türkçe karaktereleri ingilizce alfabedeki karşılıklarıyla değiştiren kodu yaz

#Yöntem 1
'''def turkce_to_ingilizce(text):
    ceviri = {
        "ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u",
        "Ç": "C", "Ğ": "G", "İ": "I", "Ö": "O", "Ş": "S", "Ü": "U"
    }
    
    for turkce, ingilizce in ceviri.items():
        text = text.replace(turkce, ingilizce)
    
    return text

# Kullanıcıdan giriş al
metin = input("Bir metin girin: ")
donusturulmus_metin = turkce_to_ingilizce(metin)

print("Dönüştürülmüş Metin:", donusturulmus_metin)'''


#Girilen bir metinde ilk üç karaktere sezar şifreleme yöntemini uygula 

'''def sezar_sifreleme(metin,anahtar=3):
    sifreli_metin= " "

metin = "sezar şifreleme tekniğini öğreniyorum"
alfabe = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]


for i in metin: '''



#Sözlükte maas diye bir alan tanımlayın sonra da bu değerin yüzde 40 zam yapılmış halini döndür.
 
maas= int(input("Maas:"))
yeni_maas= int((maas)*1.40)
print ("Yeni Maaş:" , yeni_maas)
