meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
            
d = input('введите слово:').upper()
if d in meme_dict.keys():
    print (meme_dict[d])
else: 
    print ("слово не найдено")
