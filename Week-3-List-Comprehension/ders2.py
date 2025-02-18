
#Birden yüze kadar olan sayıları bir listeye ekleme.
'''deger = []
for i in range(1,101):
    deger.append(i)

print(deger)'''   

# List comprehension ile 
# Birden yüze kadar olan sayıları bir listeye ekleme.

# formül = [değişken_adı for değişken_adı in range(1,101)]
'''my_list_1_comp = [x for x in range(1,101)]
print(my_list_1_comp) '''

# 1'den 100'e kadar olan sayılar arasında  
# Sadece 2'ye tam bölünen sayıları(çift sayıları) ekleyen kodu yazın

'''my_list_2 = []
for i in range(2,101,2):
    my_list_2.append(i)
my_list_2'''

# List comprehension ile 
# 1'den 100'e kadar olan sayılar arasında  
# Sadece 2'ye tam bölünen sayıları(çift sayıları) ekleyen kodu yazın

'''#Birinci yol
my_list_2_comp = [x for x in range(2,101)]
my_list_2_comp

#İkinci yol 
my_list_2_comp= [x for x in range(1,101) if x%2==0]
my_list_2_comp'''

# List comprehension ile 1'den 100'e kadar olan her sayının 3 katını ekleyen kodu yazınız.

'''my_list_3_comp = [x*3 for x in range(1,101) ]
my_list_3_comp'''

# List comprehension formülü 
# [değişken_adı_ve_yapılacak_işlem for değişken_adı in range(başlangıç,bitiş)]

'''my_list_3_comp = [x*3 for x in range(1,101) ]
my_list_3_comp'''


#my_word_list_1= ["Furkan", "Atlan","ybs","ztyo","ybs-3a"]
'''# Bu listenin tüm elemanlarını büyük karakterle yazdırıp
# yeni bir listeye ekleyen kodu yazınız.

sözcük = ["Furkan", "Atlan","ybs","ztyo","ybs-3a"] 
for i in sözcük:
    sözcük.append(i.upper())

yeni = [i.upper for i in sözcük]'''

#my_word_list_1_comp = [x.upper() for x in my_word_list_1]
#my_word_list_1_comp

'''gecici_liste= []

for x in my_word_list_1:
    gecici_liste.append(x.upper)'''

# Aynı kelime listesindeki a harflerini e harfi ile değiştirip 
# bu kelimeleri yeni bir listeye ekleyin (list comprehension ile yapın)

'''my_word_list_1_comp= [x.replace("a","e").replace("A","E") for x in my_word_list_1]
my_word_list_1_comp'''

# 1'den 100'e kadar olan sayılar içerisinde tek sayıları negatife dönüştüren
# çift sayıların da karesini alan ve bunları yeni bir listeye ekleyen kod 

'''tek , cift = [] , []
for x in range (1,101):
    if x%2==1:
       x*=-1 
       tek.append(x)
    else :
       x*=x
       cift.append(x) '''      
'''gecici_liste_2 = []

for x in range(1,101):
    if x%2==0:
        gecici_liste_2.append(x**2)
    else :
        gecici_liste_2.append(-x)    
gecici_liste_2 '''       


# 1'den 100'e kadar olan sayılar içerisinde tek sayıları negatife dönüştüren
# çift sayıların da karesini alan ve bunları yeni bir listeye ekleyen kod 
# List comprehension ile (list comphrension if else kullanımı) 

# formül= [x_if_hali if x_sart x_else_hali else for x in liste]

'''my_list_4_comp = [-x if x%2!=0 else x**2 for x in range(1,101)]
my_list_4_comp
print(my_list_4_comp)'''

# 1'den 100'e kadar olan tek sayılarda "tek"
# Çift sayılarda "çift" yazan kodu yazınız.
# hem normal kod hem de list comprehension ile (listeye eklemek) 


'''gecici_liste_3 = []
for x in range(1,101):
    if x%2==0:
        gecici_liste_3.append(f"Çift: {x} " )
    else:
        gecici_liste_3.append(f"Tek: {x}")      
print(gecici_liste_3)
'''

'''tek_cift_yazdirma = [print(f"Çift: {i}") if i%2==0 else print(f"Tek: {i}") for i in range(1,101)]'''


# 1'den 5'e kadar olan bir listenin değeri ile 
# 6'dan 10'a kadar olan başka bir listenin değerini çarpan kod 

#beşe , ona , sonuc = [1,2,3,4,5] , [5,6,7,8,9,10] , []

'''print("Normal kod ile gösterim")
gecici_liste_4 = []

for i in range(1,6):
    for j in range(6,11):
        print(f"i = {i} iken ve j = {j} iken i*j = {i*j}")'''

'''my_list_comp_ic_ice_dongu = [a*b for a in range(1,6) for b in range(6,11) ]
print(my_list_comp_ic_ice_dongu)'''


notlar ={"ahmet":65, "ali":28, "ayşe":78, "yusuf":15, "tuğçe":40,"kaan":50}
# Notları 50'den yüksek olan öğrencilerin isimlerini getiren kodu yazın 

print("Normal kod ile gösterim")
#dictionary.items() fonksiyonu sırasıyla key ve value değerini döndürür 
# dolayısıyla şu fonksiyonu kullanıp iki değişkene atama yaparız.
for my_key, my_value in notlar.items():
    if my_value>50:
        print(my_key)

gecenler =[my_key for my_key,my_value in notlar.items() if my_value>50 ]        




