# Utwórz następujące listy:
#
# projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
# leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
# Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:
#
# The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...
#
#
#
# Utwórz kolejną listę z datami rozpoczęcia projektów:
#
# dates = ['2016-06-23', '2016-08-29', '1994-01-01']
#
# The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...
#
#
#
# Korzystając ze "sprytnego" złożenia enumerate i zip - dodaj do komunikatu dodatkowo numer kolejny projektu rozpoczynając od 1:
#
# ...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for leader, project in zip(projects, leaders):
    print("The leader of "+ project + " is "+ leader)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for date ,leader, project in (zip(dates,projects, leaders)):
    print("The leader of "+ project + " started "+date + " is "+ leader)

print()

for i , (date ,leader, project) in enumerate(zip(dates,projects, leaders)):
    print("" + str(i+1),"- The leader of "+ project + " started "+date + " is "+ leader)