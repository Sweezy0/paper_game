#Taş kağıt makas 
import random
tas="""Taş:

---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

kagıt = '''kağıt:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''makas:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

oyun_resimleri=[tas,kagıt,makas]
kullanici_secimi=int(input('''Taş, kağıt, makas? "Taş" seçmek için "0", "kağıt" seçmek için "1" ve "makas" seçmek için "2" rakamına basın...\n'''))
if (kullanici_secimi>2 or kullanici_secimi<0):
    print("Geçersiz değer girdiniz...")
else:
    print("Seçiminiz...")
    print(oyun_resimleri[kullanici_secimi])

    bilgisayar_secimi=random.randint(0,2)
    print("Bilgisayar seçiyor...")
    print(oyun_resimleri[bilgisayar_secimi])

if kullanici_secimi==0 and bilgisayar_secimi==2:
    print("Kazandınız!")
elif bilgisayar_secimi==0 and kullanici_secimi==2:
    print("kaybettiniz!")
elif bilgisayar_secimi>kullanici_secimi:
    print("Kaybettiniz!")
elif kullanici_secimi>bilgisayar_secimi:
    print("Kazandınız!")
elif bilgisayar_secimi==kullanici_secimi:
    print("Berabere kaldınız!")