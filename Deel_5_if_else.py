"""
Soms willen we dat een stuk code zich anders gedraagd, afhankelijk van wat
voor data we hebben. Hiervoor kunnen we een if-else statement gebruiken.
(als-dan in het Nederlands)

Hieronder staat een lijst met opties, en een variabele 'gekozen optie'
Door het getal in gekozen optie te veranderen (kan 0, 1 of 2 worden) kunnen
we bepalen of de code eronder zal werken met een string, integer of float
"""
opties = ['drie', 3, 3.0]
gekozen_optie = opties[0]

""" Kijk nu eens wat er gebeurt in de onderstaande code """

if type(gekozen_optie) == str:  #(str staat voor string)
    print(gekozen_optie.upper())
else:
    print(gekozen_optie + 2)

"""
Zie je hoe de output veranderd als we een ander type data opgeven?

Er zijn veel manieren om if-else statements te bouwen. We kunnen ze zelfs 
uitbreiden met meerdere 'elif's in het midden. 
Vul hieronder je leeftijd in om dit effect in actie te zien
"""

leeftijd = 28

if leeftijd < 0:
    print("Je leeftijd is een negatief getal, dat kan niet")
elif leeftijd < 18:
    print("Je mag nog niet autorijden")
elif leeftijd < 121:
    print("Je mag autorijden als je je rijbewijs hebt!")
else:
    print("je mag in theorie autorijden maar bent waarschijnlijk zo oud dat we het niet zouden aanraden...")

