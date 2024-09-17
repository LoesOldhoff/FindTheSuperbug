voorbeeld_lijst = [4, 6, 1, 7, 8, 9, 12]

"""
Lijsten zijn bijzonder omdat de uit meerdere 'delen' bestaan.
De officiele naam hiervoor is 'iterable'
Python kan over dit soort datatypen heen 'loopen' (oftewel, dit stuk code 
meerdere keren runnen) 
Kijk hier eens naar: 
"""

for item in voorbeeld_lijst:
    print(item)

"""
(^ Die laatste zin is 'geindent' oftewel er staat een tab voor. 
Dit geeft aan dat dit stuk code bij de loop hoort. 
Haal de tab eens weg en kijk wat er gebeurt.) 

Als een lijst in een lijst zit kunnen we ook meerdere keren for-loops 
inbouwen:
"""
lijst_met_lijsten = [['een', 'losse', 'zin'], ['een', 'andere', 'zin']]

for korte_lijst in lijst_met_lijsten:
    print(korte_lijst)
    for woord in korte_lijst:
        print(woord)

""" Dit kan met lijsten maar ook met strings, omdat ook die uit meerdere
onderdelen bestaan, en dus 'itereerbaar' zijn """

lange_zin = 'the quick brown fox jumps over the lazy dog'

for letter in lange_zin:
    print(letter)

"""
Lijsten zijn handig om informatie in te bewaren, maar wat als we er weer 
informatie uit willen halen? Dat kan! De variabelen in de lijst staan op 
volgorde (van 0 tot het einde van de lijst) 

We kunnen met blokhaken achter de variabelen van de lijst items terughalen
"""

lijst_met_woorden = ['I', 'like', 'the', 'flowers', 'I', 'like', 'the', 'daffodils']

# print(lijst_met_woorden[3])
# print(lijst_met_woorden[0])
# print(lijst_met_woorden[-1])
# print(lijst_met_woorden[2:6])