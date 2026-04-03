
ogrenciler = []

while True:
    isim = input("Öğrencinin adını giriniz:")
    if not isim.isalpha():
        print("Lütfen isim giriniz.")
        continue
    notlar = input("Proje, vize, final notlarını sırasıyla birer boşluk bırakarak giriniz:").split()
    if len(notlar) != 3:
        print("Lütfen 3 adet not giriniz.")
        continue
    ortalama = int(notlar[0])*0.2 + int(notlar[1])*0.3 + int(notlar[2])*0.5
    if ortalama >= 90:
        harf_notu = "AA"
    elif ortalama >= 80:
        harf_notu = "BA"
    elif ortalama >= 70:
        harf_notu = "BB"
    elif ortalama >= 60:
        harf_notu = "CB"
    elif ortalama >= 50:
        harf_notu = "CC"
    else:
        harf_notu = "FF"

    ogrenciler.append({
        "isim": isim,
        "ortalama": ortalama,
        "harf notu": harf_notu
    })     # öğrencinin ismi alındı, notları ve harf notu ana listeye kaydedildi

    devam = input("Başka bir öğrenci eklemek isterseniz \"y\", çıkmak isterseniz herhangi bir tuşa basın:")
    if devam == "y":
        continue
    else:
        for a in ogrenciler:
            print(f"{a["isim"]}, {a["ortalama"]:.2f}, {a["harf notu"]}")
        break
