answers = {"Cevap1" : "1920",
           "Cevap2" : "Sabahattin Ali",
           "Cevap3" : "Şanlıurfa",
           "Cevap4" : "R",
           "Cevap5" : "Bandırma",
           "Cevap6" : "Simograf",
           "Cevap7" : "Berlin",
           "Cevap8" : "21 Aralık",
           "Cevap9" : "Golf",
           "Cevap10" : "50"}
total = 0
question1 = input("Soru1: TBMM hangi yilda kurulmuştur?")

if question1 == answers["Cevap1"]:
  total += 10
else:
  total += 0

question2 = input("Soru2: Kuyucaklı Yusuf adlı eser kime aittir?")

if question2 == answers["Cevap2"]:
  total += 10
else:
  total += 0

question3 = input("Soru3: Tarihin sıfır noktası olarak bilinen Göbeklitepe hangi ilimizdedir?")

if question3 == answers["Cevap3"]:
  total += 10
else:
  total += 0

question4 = input("Soru4: Bir elektrik devresinde direnç hangi harfle gösterilir?")

if question4 == answers["Cevap4"]:
  total += 10
else:
  total += 0

question5 = input("Soru5: Mustafa Kemal Atatürk'ü İstanbul'dan Samsun'a götüren vapurun adı nedir?")

if question5 == answers["Cevap5"]:
  total += 10
else:
  total += 0

question6 = input("Soru6: Depremin büyüklüğünü ve süresini ölçen alete ne ad verilir?")

if question6 == answers["Cevap6"]:
  total += 10
else:
  total += 0

question7 = input("Soru7: Almaya'nın başkenti neresidir?")

if question7 == answers["Cevap7"]:
  total += 10
else:
  total += 0

question8 = input("Soru8: En uzun gecenin yaşandığı tarih hangisidir?")

if question8 == answers["Cevap8"]:
  total += 10
else:
  total += 0


question9 = input("Soru9: Tiger Woods hangi sporun en önemli temsilcisidir?")

if question9 == answers["Cevap9"]:
  total += 10
else:
  total += 0

question10 = input("Soru10: Yerleşim yerleri içinde otomobiller için hız limiti saatte kaç kilometredir?")

if question10 == answers["Cevap10"]:
  total += 10
else:
  total += 0

if total < 50:
  print("Başarısız oldunuz. Puanınız: ",total)
else:
  print("Tebrikler. Puanınız: ",total)
