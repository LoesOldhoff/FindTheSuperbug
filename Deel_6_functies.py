"""
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
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore,
While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
Tis some visitor," I muttered, "tapping at my chamber door —
Only this, and nothing more."

Ah, distinctly I remember it was in the bleak December,
And each separate dying ember wrought its ghost upon the floor.
Eagerly I wished the morrow; — vainly I had sought to borrow
From my books surcease of sorrow — sorrow for the lost Lenore —
For the rare and radiant maiden whom the angels name Lenore —
Nameless here for evermore.

And the silken sad uncertain rustling of each purple curtain
Thrilled me — filled me with fantastic terrors never felt before;
So that now, to still the beating of my heart, I stood repeating,
Tis some visitor entreating entrance at my chamber door —
Some late visitor entreating entrance at my chamber door; —
This it is, and nothing more."

Presently my soul grew stronger; hesitating then no longer,
Sir," said I, "or Madam, truly your forgiveness I implore;
But the fact is I was napping, and so gently you came rapping,
And so faintly you came tapping, tapping at my chamber door,
That I scarce was sure I heard you"— here I opened wide the door; —
Darkness there, and nothing more.

Deep into that darkness peering, long I stood there wondering, fearing,
Doubting, dreaming dreams no mortals ever dared to dream before;
But the silence was unbroken, and the stillness gave no token,
And the only word there spoken was the whispered word, "Lenore?"
This I whispered, and an echo murmured back the word, "Lenore!" —
Merely this, and nothing more.

Back into the chamber turning, all my soul within me burning,
Soon again I heard a tapping somewhat louder than before.
Surely," said I, "surely that is something at my window lattice:
Let me see, then, what thereat is, and this mystery explore —
Let my heart be still a moment and this mystery explore; —
'Tis the wind and nothing more."

Open here I flung the shutter, when, with many a flirt and flutter,
In there stepped a stately raven of the saintly days of yore;
Not the least obeisance made he; not a minute stopped or stayed he;
But, with mien of lord or lady, perched above my chamber door —
Perched upon a bust of Pallas just above my chamber door —
Perched, and sat, and nothing more.

Then this ebony bird beguiling my sad fancy into smiling,
By the grave and stern decorum of the countenance it wore.
Though thy crest be shorn and shaven, thou," I said, "art sure no craven,
Ghastly grim and ancient raven wandering from the Nightly shore —
Tell me what thy lordly name is on the Night's Plutonian shore!"
Quoth the Raven, "Nevermore."

Much I marveled this ungainly fowl to hear discourse so plainly,
Though its answer little meaning— little relevancy bore;
For we cannot help agreeing that no living human being
Ever yet was blest with seeing bird above his chamber door —
Bird or beast upon the sculptured bust above his chamber door,
With such name as "Nevermore.”
― Edgar Allan Poe, The Raven 
'''
)