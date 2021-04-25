import random

total_weight = 0
max_weight_element_weight = 0
max_weight_element_num = 0
packages = 0
container = 0
no_elements = int(input("Podaj liczbę elementów: "))
counter = 1
sum = packages * 20 - total_weight
while counter <= no_elements:
    element_weight = int(input(f"Podaj wagę elementu: "))
    print(f"Waga elementu {counter}: {element_weight}")
    total_weight += element_weight
    container += element_weight
    if element_weight > 10:
        total_weight -= element_weight
        container -= element_weight
        element_weight = 0
        print("\nBŁĄD PROGRAMU: Wprowadź ponownie wagę!")
        continue
    if element_weight < 1 or not element_weight:
        break
    if container >= 20:
        packages += 1
        container = 0
    if container > 0 and container < 20:
        container += element_weight
        packages += 1
    if counter == no_elements:
        container = element_weight
        packages -= 1
    if element_weight > max_weight_element_weight:
        max_weight_element_weight = element_weight
        max_weight_element_num = counter
    if no_elements == counter:
        container += element_weight
        packages += 1
    counter += 1
    if sum >= 20:
        packages -= 1
    if sum < 0:
        packages += 1
    print("ELEMENT ADDED AND SHIPPED")

print(f"\nWysłano: {packages} paczek")
print(f"Liczba kilogramów wysłanych: {total_weight} kg")
print(f"W paczce {packages} było najwięcej wolnych kg: {packages * 20 - total_weight}")
print(f"Liczba pustych kg: {packages * 20 - total_weight}")
print(f"Element: {max_weight_element_num} miał najwięcej kg: {max_weight_element_weight}")
