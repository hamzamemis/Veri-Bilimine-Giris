class Insan:
    def __init__(self, isim, yas, cinsiyet):
        self.isim = isim
        self.__yas = yas
        self.cinsiyet = cinsiyet

    def bilgi_ver(self):
        print(f"Adı: {self.isim}, Yaşı: {self.__yas}, Cinsiyeti: {self.cinsiyet}")

    def get_yas(self):
        return self.__yas

    def set_yas(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas
        else:
            print("Yaş 0'dan büyük olmalı.")

    def konus(self):
        print(f"{self.isim} konuşuyor...")


class Hoca(Insan):
    def __init__(self, isim, yas, cinsiyet, brans):
        super().__init__(isim, yas, cinsiyet)
        self.brans = brans

    def konus(self):
        print(f"{self.isim} adlı hoca {self.brans} dersini anlatıyor.")


class Ogrenci(Insan):
    def __init__(self, isim, yas, cinsiyet, sinif, okul_no):
        super().__init__(isim, yas, cinsiyet)
        self.sinif = sinif
        self.__okul_no = okul_no

    def get_okul_no(self):
        return self.__okul_no

    def set_okul_no(self, yeni_no):
        if yeni_no > 0:
            self.__okul_no = yeni_no
        else:
            print("Okul numarası geçerli olmalı!")

    def katil(self):
        return f"{self.isim} adlı öğrenci {self.sinif} sınıfında derse katıldı."

    def konus(self):
        print(f"{self.isim} adlı öğrenci konuşuyor...")


class Sekreter(Insan):
    def __init__(self, isim, yas, cinsiyet, bolum):
        super().__init__(isim, yas, cinsiyet)
        self.bolum = bolum

    def evrak_isle(self):
        return f"{self.isim} adlı sekreter {self.bolum} bölümündeki evraklarla ilgileniyor."

    def konus(self):
        print(f"{self.isim} adlı sekreter konuşuyor...")


# Ana Program
insan = Insan("Ahmet", 28, "Erkek")
hoca = Hoca("Merve", 38, "Kadın", "Fizik")
ogrenci = Ogrenci("Burak", 17, "Erkek", "11-B", 305)
sekreter = Sekreter("Selin", 33, "Kadın", "Muhasebe")

insan.bilgi_ver()
hoca.bilgi_ver()
ogrenci.bilgi_ver()
sekreter.bilgi_ver()

hoca.konus()
print(ogrenci.katil())
print(sekreter.evrak_isle())

try:
    print(ogrenci.__okul_no)
except AttributeError:
    print("Hata: okul_no gizli bir özelliktir, doğrudan erişilemez!")

print(ogrenci.get_okul_no())
ogrenci.set_okul_no(400)
print(ogrenci.get_okul_no())

for kisi in [insan, hoca, ogrenci, sekreter]:
    kisi.konus()
