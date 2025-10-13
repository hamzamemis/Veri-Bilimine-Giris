# Fonksiyon Oluşturma

**Soru:** Hangisi ile fonksiyon oluşturulur?

    __init__ fonksiyon1():
    func fonksiyon1():
    def fonksiyon1():
    const fonksiyon1():
    class fonksiyon1():

**Cevap:**\
`def fonksiyon1():`

------------------------------------------------------------------------

# Tür Dönüşümü

**Soru:** Aşağıdaki işlemlerin tür dönüşümü sonrası matematiksel
işlemlerde kullanılabilmesi ve tam sayı değer vermesi için boş bırakılan
yerlere ne gelmelidir?

``` python
a = .......................(input("vize notunuzu girin = "))
```

**Cevap:**\
`int(...)`

------------------------------------------------------------------------

# Karar Yapıları

**Soru:** Aşağıdakilerden hangisi karar yapılarında kullanılan
deyimlerden birisi değildir?

    while
    continue
    if... :  elif....:  else:
    break
    def

**Cevap:**\
`def`

------------------------------------------------------------------------

# Nesne Tabanlı Programlama Kavramları

## Encapsulation (Kılıflama-Sarmalama) Nedir?

Sınıf içindeki verileri gizleyip, sadece getter ve setter metodları ile erişime açmaktır.


## Inheritance (Kalıtım) Nedir?

Bir sınıfın başka bir sınıfın özelliklerini ve metotlarını miras alarak kullanabilmesidir.
------------------------------------------------------------------------

# Nesne Tabanlı Programlama Örneği: İnsan, Öğrenci ve Hoca Sınıfları

Bu örnekte, **kalıtım (inheritance)**, **metot ezme (overriding)** ve
**çok biçimlilik (polymorphism)** prensipleri gösterilmiştir.

``` python
class Insan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.__yas = yas

    def get_yas(self):
        return self.__yas

    def set_yas(self, yeni_yas):
        if yeni_yas > 0:
            self.__yas = yeni_yas

    def konus(self):
        print(f"{self.isim} konuşuyor...")


class Hoca(Insan):
    def __init__(self, isim, yas, brans):
        super().__init__(isim, yas)
        self.brans = brans

    def konus(self):
        print(f"{self.isim} hocası {self.brans} dersini anlatıyor.")


class Ogrenci(Insan):
    def __init__(self, isim, yas, sinif):
        super().__init__(isim, yas)
        self.sinif = sinif

    def konus(self):
        print(f"{self.isim} adlı öğrenci {self.sinif} sınıfında derse katılıyor.")


# Örnek kullanım
insan = Insan("Ali", 30)
hoca = Hoca("Ayşe", 40, "Matematik")
ogrenci = Ogrenci("Mehmet", 15, "10-A")

for kisi in [insan, hoca, ogrenci]:
    kisi.konus()

```

------------------------------------------------------------------------

# Çalışan Sınıfları ve Soyut Sınıf Örneği

Bu örnekte, **kalıtım**, **metot ezme (overriding)** ve **soyut sınıflar
(abstract classes)** kullanılmıştır. Soyut sınıflar için `abc` modülünü
kullanıyoruz.

``` python
from abc import ABC, abstractmethod

class Calisan(ABC):
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    @abstractmethod
    def calis(self):
        pass


class MaviYaka(Calisan):
    def __init__(self, isim, yas, vardiya=3):
        super().__init__(isim, yas)
        self.vardiya = vardiya

    def calis(self):
        print(f"{self.isim} tezgahta/fabrika içinde çalışıyor ({self.vardiya} vardiya).")


class BeyazYaka(Calisan):
    def __init__(self, isim, yas, vardiya=2):
        super().__init__(isim, yas)
        self.vardiya = vardiya

    def calis(self):
        print(f"{self.isim} masabaşı çalışıyor ({self.vardiya} vardiya).")


# Örnek kullanım
mavi = MaviYaka("Ahmet", 28)
beyaz = BeyazYaka("Ayşe", 35)

mavi.calis()
beyaz.calis()

```
