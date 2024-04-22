voorbeeld_string = 'Hallo hier ben ik'

"""
Met bepaalde datatypen kunnen we bepaalde acties uitvoeren, dit zijn 'methoden'
We roepen ze aan door een punt achter de variabelenaam te zetten. 
Maar let op! Niet alle methoden werken met alle datatypen!

De methode 'upper' kan bijvoorbeeld de letters in een string in uppercase
(hoofdletters) zetten. ('lower' doet het tegenovergestelde)
"""

print(voorbeeld_string.upper())

"""
Zouden we dit ook kunnen doen met een getal? Wat denk je?
Verwijder de hashtag om de code te activeren en probeer het uit
"""

# print(voorbeeld_int.upper())

"""
Als het goed is heb je net een error gezien. Net zoals wij niet weten hoe je
een hoofdletter zou maken van een getal, weet Python dat ook niet

Hier zijn nog wat methoden. Zet deze in 'print()' om ze te kunnen zien
"""

voorbeeld_string.lower()
voorbeeld_string.swapcase()
voorbeeld_string.title()

""" 
Let op! Sommige methoden hebben meer informatie nodig om te kunnen werken
bijvoorbeeld 'replace' die bepaalde onderdelen van een string kan vervangen
Echter, voordat replace kan werken moet het weten wat het moet vervangen, 
en waarin

probeer de twee argumenten in de replace methode eens te veranderen, en kijk 
wat er gebeurt (vergeet niet te printen)
"""
voorbeeld_string.replace('e', 'eeeeeeee')

"""
Python heeft ook functies die niet per se bij een datatype horen. Deze kan je 
op ieder moment aanroepen, maar ze hebben wel bijna altijd argumenten nodig 

een voorbeeld dat je al gezien hebt is 'print()', het argument is dat wat 
je wil printen

hieronder staan nog wat voorbeelden. Kan je bedenken wat ze doen voor je ze 
uitvoert?
"""

# len(voorbeeld_string)
# type(voorbeeld_string)
# type(50)
# type(0.5)

