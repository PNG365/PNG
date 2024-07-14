cool_list = {
    "LOL": "Komik bir şeye verilen cevap.",
    "GAMING": "Oyuncuların oyun oynamak anlamına gelen kullandıkları kelime.",
    "FF": "koruyucu kalkan.",
            }
word = input("Anlamadığınız bir kelime yazın. (Hepsini büyük harflerle yazınız)")
if word in cool_list.keys():
    print(cool_list[word])
else:
    print("Kelime sözlükte yok.")
