# Napisz program do obsługi ładowarki paczek.
# Każda paczka może maksymalnie zmieścić 20 kg towaru.
# Do paczki dodawane są elementy. Każdy z nich może ważyć od 1 do 10 kg.
# Jeśli dodanie elementu do paczki zwiększyłoby ciężar paczki powyżej 20kg,
# paczka powinna zostać wysłana (nie można już do niej dodać w przyszłości elementów),
# a bieżący element powinien zostać dodany do nowej paczki.
# Wszystkie elementy powinny zostać wysłane.
# Program powinien pobierać maksymalną liczbę elementów do wysyłki.
# Jeśli podano element o wadze 0, program powinien zakończyć działanie,
# tak jakby maksymalna liczba paczek została osiągnięta.
# Na koniec działania program powinien wyświetlić w podsumowaniu:

# Liczbę paczek wysłanych
# Liczbę kilogramów wysłanych
# Suma "pustych" - kilogramów (brak optymalnego pakowania).
# Liczba paczek * 20 - liczba kilogramów wysłanych
# Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
# Program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg,
# lub mniej niż 1 kg i nie był dokładnie równy 0.

import random

# Zmienne:

no_elements = int(input("Liczba elementów do wysłania: "))

counter = 1
total_weight = 0

max_weight_element_weight = 0
max_weight_element_num = 0

packages = 0
container = 0

free_place = 0

x = 0

while counter <= no_elements:
    element_weight = int(input(f"Podaj wagę elementu: ")) # or random.randint(1, 10)
    total_weight += element_weight
    container += element_weight
    for i in range(1, ):
        x += 1
    print(f"Waga elementu {x}: {element_weight}")

    if element_weight > 10:
        total_weight -= element_weight
        container -= element_weight
        element_weight = 0
        x -= 1
        print("\nBŁĄD PROGRAMU: Wprowadź ponownie wagę!")
        continue

    if element_weight < 1 and element_weight >= 0:
        break

    if container >= 20:
        packages += 1
        container = 0

    if container < 20 and counter == no_elements:
        packages += 1

    if element_weight > max_weight_element_weight:
        max_weight_element_weight = element_weight
        max_weight_element_num = counter

    if not element_weight:
        break

    counter += 1

print(f"\nWysłano: {packages} paczek")
print(f"Liczba kilogramów wysłanych: {total_weight} kg")
print(f"W paczce {packages} było najwięcej wolnych kg: {packages * 20 - total_weight}")
print(f"Liczba pustych kg: {packages * 20 - total_weight}")
print(f"Element: {max_weight_element_num} miał najwięcej kg: {max_weight_element_weight}")
