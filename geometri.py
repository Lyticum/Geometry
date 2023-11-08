from math import pi

program = True
while program:
    şekil =input("Lütfen geometrik şekli giriniz; ").lower()
    işlem=input("Lütfen yapmak istediğiniz işlemi giriniz; ").lower()
    if şekil=="kare" and işlem=="çevre":
        a= int(input("Lütfen kenar uzunluğunu giriniz; "))
        kare_çevre= 4*a
        print(kare_çevre)
    elif şekil=="eşkenar" and işlem=="çevre":
        e= int(input("Lütfen kenar uzunluğunu giriniz; "))
        eş_çevre=4*e
        print(eş_çevre)
    elif şekil=="dikdörtgen" and işlem=="çevre":
        d1= int(input("Lütfen 1.kenar uzunluğunu giriniz; "))
        d2= int(input("Lütfen 2.kenar uzunluğunu giriniz; "))
        dikdörtgen_çevre=2*(d1+d2)
        print(dikdörtgen_çevre)
    elif şekil=="paralelkenar" and işlem=="çevre":
        p1= int(input("Lütfen 1.kenar uzunluğunu giriniz; "))
        p2= int(input("Lütfen 2.kenar uzunluğunu giriniz; "))
        paralel_çevre=2*(p1+p2)
        print(paralel_çevre)
    elif şekil=="üçgen" and işlem=="çevre":
        ü1= int(input("Lütfen 1.kenar uzunluğunu giriniz; "))
        ü2= int(input("Lütfen 2.kenar uzunluğunu giriniz; "))
        ü3= int(input("Lütfen 3.kenar uzunluğunu giriniz; "))
        çevre_üçgen = ü1+ü2+ü3
        print(çevre_üçgen)
    elif şekil=="yamuk" and işlem=="çevre":
        y1= int(input("Lütfen 1.kenar uzunluğunu giriniz; "))
        y2= int(input("Lütfen 2.kenar uzunluğunu giriniz; "))
        y3= int(input("Lütfen 3.kenar uzunluğunu giriniz; "))
        y4= int(input("Lütfen 4.kenar uzunluğunu giriniz; "))
        çevre_yamuk = y1+y2+y3+y4
        print(çevre_yamuk)
    elif şekil=="daire" and işlem=="çevre":
        r= int(input("Lütfen yarıçap uzunluğunu giriniz; "))
        daire_çevre= 2*round(pi, 2)*r
        print(daire_çevre)

    elif şekil=="kare" and işlem=="alan":
        a= int(input("Lütfen kenar uzunluğunu giriniz; "))
        kare_alan= a ** 2
        print(kare_alan)
    elif şekil=="eşkenar" and işlem=="alan":
        k1= int(input("Lütfen köşegen uzunluğunu giriniz; "))
        k2= int(input("Lütfen köşegen uzunluğunu giriniz; "))
        eş_alan=(k1 * k2)/2
        print(eş_alan)
    elif şekil=="dikdörtgen" and işlem=="alan":
        d1= int(input("Lütfen 1.kenar uzunluğunu giriniz; "))
        d2= int(input("Lütfen 2.kenar uzunluğunu giriniz; "))
        dikdörtgen_alan=d1*d2
        print(dikdörtgen_alan)
    elif şekil=="paralelkenar" and işlem=="alan":
        p1= int(input("Lütfen taban uzunluğunu giriniz; "))
        p2= int(input("Lütfen yüksekliği giriniz; "))
        paralel_alan=p1*p2
        print(paralel_alan)
    elif şekil=="üçgen" and işlem=="alan":
        ü1= int(input("Lütfen taban uzunluğunu giriniz; "))
        ü2= int(input("Lütfen yüksekliği giriniz; "))
        alan_üçgen = (ü1*ü2)/2
        print(alan_üçgen)
    elif şekil=="yamuk" and işlem=="alan":
        y1= int(input("Lütfen üst kenar uzunluğunu giriniz; "))
        y2= int(input("Lütfen alt kenar uzunluğunu giriniz; "))
        y3= int(input("Lütfen yüksekliği giriniz; "))
        alan_yamuk = (y1+y2)*y3/2
        print(alan_yamuk)
    elif şekil=="daire" and işlem=="alan":
        r= int(input("Lütfen yarıçap uzunluğunu giriniz; "))
        daire_alan= round(pi, 2)* (r **2)
        print(daire_alan)

    else:
        liste = input("Hangi listeyi görmek istersiniz? (g: Geometri, i: İşlemler): ").lower()

        if liste == "g":
            geometri = ["Kare", "Dikdörtgen", "Üçgen", "Paralelkenar", "Eşkenar dörtgen", "Yamuk", "Daire"]
            for i in geometri:
                print(i)
        elif liste == "i":
            işlemler = ["Çevre", "Alan"]
            for i in işlemler:
                print(i)
        else:
            print("Geçersiz seçenek! 'g' veya 'i' giriniz.")
    
    çıkış=input("Programdan çıkmak için 'Q''e basınız;").lower()
    if çıkış == "q":
        program=False
        print("İyi günler!")
    else:
        program=True
    






        