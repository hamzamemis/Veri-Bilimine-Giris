class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"Ben bir insanım, adım {self.ad}.")


class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self):
        print(f"Ben hoca {self.ad}, ders anlatıyorum.")

    def ders_ver(self):
        print(f"Hoca {self.ad} (Sicil No: {self.sicil_no}) şu anda ders veriyor.")


class Sekreter(Insan):
    def __init__(self, ad, yas, departman):
        super().__init__(ad, yas)
        self.departman = departman

    def konus(self):
        print(f"Ben sekreter {self.ad}, {self.departman} departmanında çalışıyorum.")

    def randevu_ayarla(self):
        print(f"Sekreter {self.ad}, bir randevu ayarladı.")


class Ogrenci(Insan):
    def __init__(self, ad, yas, ogrenci_no):
        super().__init__(ad, yas)
        self.ogrenci_no = ogrenci_no

    def konus(self):
        print(f"Ben öğrenci {self.ad}, ders çalışıyorum.")

    def ders_calıs(self):
        print(f"Öğrenci {self.ad} (No: {self.ogrenci_no}) ders çalışıyor.")


# --- Örnek Kullanım ---
hoca1 = Hoca("Ahmet", 40, 1905)
sekreter1 = Sekreter("Zeynep", 33, "Eğitim")
ogrenci1 = Ogrenci("Ali", 18, 129)

hoca1.konus()
hoca1.ders_ver()

sekreter1.konus()
sekreter1.randevu_ayarla()

ogrenci1.konus()
ogrenci1.ders_calıs()
