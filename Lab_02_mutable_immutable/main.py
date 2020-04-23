# LAB - Typy zmienne (mutable) i niezmienne (immutable)
# Oto deklaracja zmiennej days:
#
# days = ['mon','tue','wed','thu','fri','sat','sun']
#
# należy utworzyć zmienną workdays, która początkowo będzie zawierać te same elementy co days
#
# następnie należy usunąć z workdays dni wolne
#
# na koniec wyświetl days i workdays i upewnij się, że sobota i niedziela zniknęły tylko z listy workdays

days = ['mon','tue','wed','thu','fri','sat','sun']
work_days = days.copy()

work_days.remove('sat')
work_days.remove('sun')

print(days)
print(work_days)