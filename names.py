print("Mam na imię Łukasz Laba")  # tutaj wpisz swoje imię

# Wyznaczyć 18 list pierwszych za pomocą Python.
# Przedstawić obrazowo binarny zapis tych liczb w ciekawy sposób.

# wyznaczenie listy liczb pierwszych
prime_counter = 0
prime_list = []
i = 1
while prime_counter < 18:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            continue
    if is_prime:
        prime_list.append(i)
        prime_counter += 1
    i += 1
print('\nLista list pierwszych:')
print(prime_list)

#tworzenie obrazka
print('\nPierwszoliczbowa binarna choinka świąteczna z dydykacją dla Prowadzącego :)\n')
for i in prime_list + [1,1]: # dodatkowe [1,1] to nóżka
    prime_sting = '{:012b}'.format(i)
    prime_sting = prime_sting.replace('1', ' X ').replace('0', '   ')
    print(prime_sting + prime_sting[::-1], '   ', i) #wyswietlennie prime_sting z dołączonym lustrzanym odbiciem
print(2 * 12 * ' - ')





