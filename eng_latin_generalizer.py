from engsyllabifier import *
from latinsyllabifier import *

def generalize_latin(syllable):
    syllable = syllable.replace("k","c")
    syllable = syllable.replace("ch","c")
    return syllable

def generalize_eng(syllable):
    #eng > latin
    #(need to be able to map to multiple chars)
    #vowels:
    syllable = syllable.replace("AA","a")
    syllable = syllable.replace("AH","a")
    syllable = syllable.replace("AE","a")
    #syllable.replace("AO","a") #alternate
    syllable = syllable.replace("EH","e")
    syllable = syllable.replace("IH","e") #duplicate
    syllable = syllable.replace("IY","i")
    #syllable.replace("IH","i") #aternate
    syllable = syllable.replace("OW","o")
    syllable = syllable.replace("UH","o") #duplicate
    syllable = syllable.replace("AO","o") #duplicate
    syllable = syllable.replace("UW","u")
    syllable = syllable.replace("ER","u")
    #syllable.replace("UH","u") #aternate
    syllable = syllable.replace("AY","ae")
    syllable = syllable.replace("AW","au")
    syllable = syllable.replace("EY","ei")
    syllable = syllable.replace("OY","oe")

    #consonents:
    syllable = syllable.replace("KW","qu")
    syllable = syllable.replace("DH","th")
    syllable = syllable.replace("TH","th")
    syllable = syllable.replace("K","c")
    syllable = syllable.replace("CH","c")
    syllable = syllable.replace("ZH","s")
    syllable = syllable.replace("SH","s")
    syllable = syllable.replace("NG","g")
    syllable = syllable.replace("JH","g")
    syllable = syllable.replace("HH","h")
    syllable = syllable.replace("Y","i")
    syllable = syllable.replace("W","v")
    syllable = syllable.lower()
    return syllable

def compare(e_source, l_source):
    with open(e_source, 'r') as e_file:
        english  = e_file.read()

    with open(l_source, 'r') as l_file:
        latin = l_file.read()

    e_syllables = e_syllabifier(english)
    l_syllables = syllabifier(latin)

    for syl in e_syllables:
        print(syl)
        for s in syl:
            print(s)
            x = generalize_eng(s)
            x = generalize_latin(x)
            print(x)
            print(s)

    for syl in l_syllables:
        print(syl)
        for s in syl:
            print(s)
            print(generalize_latin(s))
            print(s)

    #for e_lines
    #    for l_lines
    #        if bigram match
    #            explore around
compare('wordsworth #1.txt', 'latin.txt')