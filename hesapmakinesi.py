import math
import re

def toplama(x, y):
  return x + y

def cikarma(x, y):
  return x - y

def carpma(x, y):
  return x * y

def bolme(x, y):
  return x / y

def sin(x):
  return math.sin(x)

def cos(x):
  return math.cos(x)

def tan(x):
  return math.tan(x)

def log(x):
  return math.log(x)

def karekok(x):
  return math.sqrt(x)

def is_number(text):
  pattern = re.compile("[0-9.]+")
  return pattern.match(text)

def main():
  while True:
    # Kullanıcıdan işlem seçmesini isteyin
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Sinüs")
    print("6. Kosinüs")
    print("7. Tanjant")
    print("8. Logaritma")
    print("9. Karekök")
    print("0. Çıkış")

    try:
      secim = int(input("Seçiminiz: "))
    except ValueError:
      print("Hata 102: Geçersiz seçim.")
      continue

    if secim not in range(11):
      print("Hata 102: Geçersiz seçim.")
      continue

    # Kullanıcıdan sayıları isteyin
    if secim in [1, 2, 3, 4]:
      try:
        x = float(input("Birinci sayıyı giriniz: "))
        y = float(input("İkinci sayıyı giriniz: "))
      except ValueError:
        print("Hata 101: Geçersiz sayı girişi.")
        continue

    else:
      try:
        x = float(input("Sayıyı giriniz: "))
      except ValueError:
        print("Hata 101: Geçersiz sayı girişi.")
        continue


    # Seçilen işleme göre fonksiyonu çağırın ve sonucu yazdırın
    if secim == 1:
      sonuc = toplama(x, y)
      print(f"{x} + {y} = {sonuc}")
    elif secim == 2:
      sonuc = cikarma(x, y)
      print(f"{x} - {y} = {sonuc}")
    elif secim == 3:
      sonuc = carpma(x, y)
      print(f"{x} * {y} = {sonuc}")
    elif secim == 4:
      sonuc = bolme(x, y)
      print(f"{x} / {y} = {sonuc}")
    elif secim == 5:
      sonuc = sin(x)
      print(f"sin({x}) = {sonuc}")
    elif secim == 6:
      sonuc = cos(x)
      print(f"cos({x}) = {sonuc}")
    elif secim == 7:
      sonuc = tan(x)
      print(f"tan({x}) = {sonuc}")
    elif secim == 8:
      sonuc = log(x)
      print(f"log({x}) = {sonuc}")
    elif secim == 9:
      sonuc = karekok(x)
      print(f"√({x}) = {sonuc}")
    else:
      break

    # İşlem bittikten sonra devam etmek isteyip istemediğini sor
    devam = input("Devam etmek ister misiniz? (e/h): ")

    if devam.lower() == "h":
      print("Bizi kullandığınız için teşekkürler")
      break

if __name__ == "__main__":
  main()