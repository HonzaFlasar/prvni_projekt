# seznam uživatelů
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
oddelovac = "***"

# zadání uživatelského jména a hesla
username = input("Username: ")
password = input("Password: ")

# ověření jména a hesla dle seznamu users
if users.get(username) == password:

# přivítání registrovaného uživatele
    print(oddelovac)
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print(oddelovac)
# nebo ukončení
else:
    print("Unregistered user, terminating the program..")
    quit()

'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# výběr ze tří textů
vyber_textu = input("Enter a number btw. 1 and 3 to select: ")

# zjištění, zda se jedná o číslo a zda je v požadovaném intervalu
if vyber_textu.isnumeric():
    cislo_textu = int(vyber_textu)
    if cislo_textu in range(1,4):
      print("Text no. ", cislo_textu)

    # číslo jiné než přiřazené - konec
    else:
        print("Wrong number, terminating the program..")
        quit()
# jiný znak než číslo - konec:
else:
    print("Not a number, terminating the program..")
    quit()

index_textu = cislo_textu - 1
#print(TEXTS[index_textu])

# rozdělení textu na slova
slova = TEXTS[index_textu].split()
vycistena_slova = []
for slovo in slova:
    vycistena_slova.append(slovo.strip(",.:;!?"))

# Slovník s počtem výskytu jednotlivých typů písmen
counts = {"velke": 0, "male": 0, "prvni_velke": 0, "cislo": 0}
# počet slov
print("There are ", (len(slova)), "words in the selected text.")

# iterace slov ve větě
for slovo in slova:

# počet slov malými písmeny
    if slovo.islower():
        counts["male"] += 1

# počet slov velkými písmeny
    elif slovo.isupper():
        counts['velke'] += 1

# počet slov začínajících velkým písmenem
    elif slovo.istitle():
        counts["prvni_velke"] += 1

    # počet čísel
    else:
        if slovo.isnumeric():
            counts["cislo"] += 1
        else:
            continue

# zobrazení výsledků
print("There are ", counts["prvni_velke"], "titlecase words.")
print("There are ", counts["velke"], "uppercase words.")
print("There are ", counts["male"], "lowercase words.")
print("There are ", counts["cislo"], "numeric strings.")

# součet všech čísel
soucet = 0
for slovo in slova:
    if slovo.isnumeric():
        citatel = int(slovo)
        soucet = soucet + citatel
    else:
        continue
print("The sum of all the numbers ", soucet)

# zjištění četnosti délek slov
cetnost_delek = {}
for slovo in slova:
    delka = len(slovo)
    if delka not in cetnost_delek:
        cetnost_delek[slovo] = 1
    else:
        cetnost_delek[slovo] = cetnost_delek[slovo] + 1
#print(cetnost_delek)

# zjištění četnosti délek slov
cetnost_delek = {}
for slovo in vycistena_slova:
    delka = len(slovo)
    if delka not in cetnost_delek: #pokud délka není ve slovníku, přidej ji
        cetnost_delek[delka] = 1
    else:
        cetnost_delek[delka] = cetnost_delek[delka] + 1 #jinak přičti jednu

#pprint(cetnost_delek)
pocty_delek = list(cetnost_delek.values())
#print(pocty_delek)

cara = "+---+-------------------+----+"
print(oddelovac)
print("")
print("Len |    Occurences     | Nr.|")

for key, value in sorted(cetnost_delek.items()):
    hvezdicky = ("*" * (value))
    print(cara, f"|{key:^3}| {hvezdicky:17} | {value:^3}| ", sep="\n")







