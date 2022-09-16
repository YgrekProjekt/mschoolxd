import random
import os

dict = {
"blouse":"bluzka",
"bra":"biustonosz",
"button":"guzik",
"caroligan":"sweter rozpinany",
"coat":"plaszcz",
"collar":"kołnież",
"cuff":"mankiet",
"dressing-gown":"szlafrok",
"jacket":"kurtka",
"jumper":"sweter",
"knickers":"majtki",
"nightie":"koszula nocna",
"pocket":"kieszen",
"polo-neck":"golf (sweter)",
"rain coat":"płaszcz przeciw deszczowy",
"shirt":"koszulka",
"sleeve":"rękaw",
"scruffy":"niechlujny",
"socks":"skarpety",
"sweatshirt":"bluza dresowa",
"top":"top",
"tracksuit":"dres",
"underpants":"kalesony",
"underwear":"bielizna",
"waistcoat":"kamizelka",
"zip":"zamek",
"boots":"buty wysokie",
"flip-flops":"klapki (japonki)",
"slippers":"klapki",
"cotton":"bawełnianie",
"denim":"jeansowe",
"leather":"skórzane",
"linen":"lniany/płócienny",
"silk":"jedwabne",
"wool":"wełniane",
"thight fitting jacket":"dopasowana kurtka",
"checked (wzór na ubraniu)":"w kratkę (wzór na ubraniu)",
"plain (wzór na ubraniu)":"czyste (wzór na ubraniu)",
"spotted (wzór na ubraniu)":"w kropki(wzór na ubraniu)",
"stripped (wzór na ubraniu)":"w prążki (wzór na ubraniu)"}



while True:
    try:
        os.system("clear")
        print("========================")       
        key = (random.choice(list(dict.value())))
        print(value)
        print("========================")
        input("Anwser: ")
        print("========================")        
        print(dict[key])
        del dict[key]
        print("========================")
        input()
    except:
        exit()
