"""
Computers zijn erg snel, maar ook erg dom. Om een computer goede
instructies te geven moet je erg precies zijn.

Python kan een paar 'typen' data herkennen:
- hele getallen (integers of ints)
- kommagetallen (floats)
- Booleans ('schakelaars', kunnen aan of uit staan (True of False)
- Zinnen en woorden (strings)

Er zijn meer typen, maar dit zijn de belangrijkste
"""

voorbeeld_int = 5
voorbeeld_float = 0.3
voorbeeld_string = 'Hallo'

""" 
Lijsten zijn ook een bepaald type data, je kan ze herkennen aan 
de blokhaken []
Lijsten zijn bijzonder omdat je er dingen in kan stoppen van andere
typen
"""

voorbeeld_lijst = [0, 4, 0.3, 'heey']
""" 
We hoeven de dingen die we in een lijst stoppen niet helemaal uit
te schrijven. We kunnen ook verwijzen naar getallen of woorden die 
we al eerder in ons script gebruikt hebben. 
"""

tweede_voorbeeld_lijst = [voorbeeld_int, voorbeeld_string]

""" Wat denk je dat hier zal gebeuren? 
Run dit script met F5 en typ print(tweede_voorbeeld_lijst) in de terminal
"""

""" Je kan naar stukken data verwijzen bij hun naam 
(witte tekst, ookwel de 'variabele' of 'variabele naam'
Ze zijn oneindig vaak te bebruiken, en je kan er maffe dingen 
mee doen
"""

nog_een_voorbeeld_lijst = [voorbeeld_lijst, voorbeeld_int, voorbeeld_string]
""" Wat zou er gebeuren met deze lijst? Kan je python het laten printen?"""

"""
Met sommige data kan je rekenen, en met andere niet 
Kijk eens of je kan bedenken wat er zal gebeuren met deze stukken code als 
je ze runt:

(Verwijder de hashtags om de code te activeren)
"""

# print(voorbeeld_float + voorbeeld_int)
# print(voorbeeld_int - voorbeeld_float)
# print(voorbeeld_lijst + voorbeeld_int)
# print(voorbeeld_lijst + voorbeeld_lijst)
# print(voorbeeld_lijst * voorbeeld_int)
# print(voorbeeld_string * voorbeeld_int)
# print(voorbeeld_string - voorbeeld_int)
