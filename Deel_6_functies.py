"""
Let op: De moeilijkheidsgraat gaat nu wat omhoog. Zorg dat je alle
voorgaande concepten snaps voordat je nu doorgaat.

We hebben nu een aantal losse onderdelen gezien. Er zijn uiteraard meer
structuren binnen python (en andere programmeertalen) maar dit zijn de
belangrijkste

Maar hoe we ze aan elkaar binden is belangrijker dan de basisstructuren.
Zie de losse onderdelen van python als de legoblokjes, waarmee we vervolgens
torens kunnen bouwen.

Een structuur die ons daarbij kan helpen is de functie
"""

def voorbeeld_functie(getal):
    return getal + 1

print(voorbeeld_functie(5))

"""
Je kan alle structuren die je tot nu toe gezien hebt samenvoegen in functies, 
die je vervolgens oneindig kan hergebruiken
"""

def analyseer_zin(zin):
    if not type(zin) == str:
       print('Dit is geen zin, hier kan ik niks mee')
    else:
        a_teller = 0
        letter_teller = 0
        alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        geen_letters = ""
        for letter in zin:
            if letter == 'a' or letter == 'A':
                a_teller = a_teller + 1
            if letter in alfabet:
                letter_teller = letter_teller + 1
            else:
                geen_letters = geen_letters + letter

        print("Deze zin is ", letter_teller, " letters lang")
        print("De letter 'A' kwam ", a_teller, " keer voor")
        print("Overige tekens die we hebben gevonden zijn: ", geen_letters)


analyseer_zin(''' 
[Songtekst van "Europapa"]

[Intro: Joost]
Europe, let's come together
(Euro-pa-pa, Euro-pa-pa)
It's now or never
I love you all (Euro-pa-pa, Euro-pa-pa)

[Chorus: Joost]
Welkom in Europa, blijf hier tot ik dood ga
Euro-pa-pa, Euro-pa-pa
Welkom in Europa, blijf hier tot ik dood ga
Euro-pa-pa, Euro-pa-pa

[Verse 1: Joost]
Bezoek m'n friends in France of neem de benen naar Wenen
Ik wil weg uit Netherlands, maar m'n paspoort is verdwenen
Heb gelukkig geen visum nodig om bij je te zijn
Dus neem de bus naar Polen of de trein naar Berlijn
Ik heb geen geld voor Paris, dus gebruik m'n fantasie
Heb je een еuro'tje, please? Zеg "merci" en "alsjeblieft"
Ik ben echt alles kwijt behalve de tijd
Dus ben elke dag op reis want de wereld is van mij

[Chorus: Joost]
Welkom in Europa, blijf hier tot ik dood ga
Euro-pa-pa, Euro-pa-pa
Welkom in Europa, blijf hier tot ik dood ga
Euro-pa-pa, Euro-pa-pa

[Post-Chorus: Joost]
Euro-pa-pa, pa-pa, pa-pa-pa
Euro-pa-pa-pa (Hey)
Euro-pa-pa, pa-pa, pa-pa-pa
Eu-ro-pa (Hey)

[Verse 2: Joost]
Ich bin in Deutschland, aber ich bin so allein
Io sono in Italia, maar toch doet het pijn
Ben aan het vluchten van mezelf, roep de hele dag om help
Ja, ik geef zelfs mensen geld, maar d'r is niemand die me helpt
Ik hoef geen escargots, hoef geen fish 'n' chips
Hoef geen paella, no, ik weet niet eens echt wat dat is
Zet de radio aan, ik hoor Stromae met "Papaoutai"
Zal niet stoppen, tot ze zeggen, "Ja, ja, dat doet 'ie goed, ey"

[Chorus: Joost]
Welkom in Europa, blijf hier tot ik dood ga
Euro-pa-pa, Euro-pa-pa
Welkom in Europa, blijf hier tot ik dood ga
Euro-pa-pa, Euro-pa-pa

[Post-Chorus: Joost]
Euro-pa-pa, pa-pa, pa-pa-pa
Euro-pa-pa-pa (Hey)
Euro-pa-pa, pa-pa, pa-pa-pa
Eu-ro-pa (Hey)
[Bridge: Joost & Tim Haars]
Europa, pa-pa-pa-pa-pa, pa-pa-pa-pa-pa
Pa-pa-pa, pa-pa-pa-pa-pa
Pa-pa-pa, pa-pa-pa-pa-pa
Pa-pa-pa, pa-pa-pa-pa-pa
Pa-pa-pa, pa-pa-pa-pa-pa
Pa-pa-pa, pa-pa-pa-pa-pa (Ja-ha)
Pa, pa, pa, pa (Hey)
Welkom in Europa, jongen!

[Drop: Joost]
(Hey)
Eu-ro-pa
'''
)