'''LAB - Skrócona składnia instrukcji if i polecenie pass
Zapisz poniższe polecenie if w postaci uproszczonej:

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)


Zapisz poniższe polecenie if w postaci uproszczonej:

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')


Ktoś był kiedyś niezadowolony, bo w kursie jest za mało polskich akcentów, więc... posłuchaj piosenki De Mono - Niedziela będzie dla nas - https://www.youtube.com/watch?v=lmn0Qf1_eI4 (możesz też skorzystać z oryginalnej wersji: Niebiesko Czarnych: https://www.youtube.com/watch?v=Fxkhe8GqYkc)

Napisz program, który:

zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia

bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić

Przepisz powyższy program stosując składnie uproszczona polecenia if'''

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)
price = 123
bonus = 23

print(price - bonus) if bonus_granted else print(price)

today_weekday = 'thursday'

tasks = {'monday':'traning', 'tuesday':'programming', 'wednesday':'cycling', 'thursday':'jogging', 'friday':'party'}

print(tasks['monday']) if today_weekday=='monday' else print(tasks['tuesday']) if today_weekday =='tuesday' else print(tasks['wednesday']) if today_weekday=='wednesday' else print(tasks['thursday']) if today_weekday=='thursday' else print(tasks['friday'])
