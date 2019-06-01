from engsyllabifier import *
from latinsyllabifier import *
from collections import Counter

def generalize_latin(syllable):
    syllable = syllable.replace("k","c")
    syllable = syllable.replace("ch","c")
    return syllable

def generalize_eng(syllable):
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
    syllable = syllable.replace("X","cs")
    syllable = syllable.replace("Z","ds")
    syllable = syllable.lower()
    return generalize_latin(syllable)

def listOlists_combiner(listOlists):
    if len(listOlists) == 0:
        return []
    else:
        return listOlists[0]+listOlists_combiner(listOlists[1:])

def syl_count(e_source, l_source):
    e_count = 0
    l_count = 0
    gen_e_syllables = []
    gen_l_syllables = []

    with open(e_source, 'r') as e_file:
        english  = e_file.read()

    with open(l_source, 'r') as l_file:
        latin = l_file.read()

    e_syllables = e_syllabifier(english)
    l_syllables = syllabifier(latin)

    for line in e_syllables:
        gen_syl = []
        for syl in line:
            e_count += 1
            x = generalize_eng(syl)
            gen_syl.append(x)
        gen_e_syllables.append(gen_syl)

    for line in l_syllables:
        gen_syl = []
        for syl in line:
            l_count += 1
            x = generalize_latin(syl)
            gen_syl.append(x)
        gen_l_syllables.append(gen_syl)

    print("Total # of Syllables in: " + l_source)
    print(l_count)
    print("Total # of Syllables in: " + e_source)
    print(e_count)
    print()

    print("Pre-generalized:")
    all_l = listOlists_combiner(l_syllables)
    print("Syllables and their Occurences in: " + l_source)
    print(Counter(all_l).most_common(25))
    all_e = listOlists_combiner(e_syllables)
    print("Syllables and their Occurences in: " + e_source)
    print(Counter(all_e).most_common(25))
    print()

    print("Generalized:")
    all_l = listOlists_combiner(gen_l_syllables)
    print("Syllables and their Occurences in: " + l_source)
    print(Counter(all_l).most_common(25))
    all_e = listOlists_combiner(gen_e_syllables)
    print("Syllables and their Occurences in: " + e_source)
    print(Counter(all_e).most_common(25))
    print()

def syl_score(e_source, l_source, score_limit):
    gen_e_syllables = []
    gen_l_syllables = []

    with open(e_source, 'r') as e_file:
        english = e_file.read()

    with open(l_source, 'r') as l_file:
        latin = l_file.read()

    e_syllables = e_syllabifier(english)
    l_syllables = syllabifier(latin)

    for line in e_syllables:
        gen_syl = []
        for syl in line:
            x = generalize_eng(syl)
            x = generalize_latin(x)
            gen_syl.append(x)
        gen_syl = set(gen_syl)
        gen_e_syllables.append(gen_syl)

    for line in l_syllables:
        gen_syl = []
        for syl in line:
            x = generalize_latin(syl)
            gen_syl.append(x)
        gen_syl = set(gen_syl)
        gen_l_syllables.append(gen_syl)

    l_line_num = 0
    for l_line in gen_l_syllables:
        l_line_num += 1
        e_line_num = 0
        for e_line in gen_e_syllables:
            e_line_num += 1
            score = 0
            for l_syl in l_line:
                for e_syl in e_line:
                    if e_syl == l_syl:
                        score += 1
            if score >= score_limit:
                print(score)
                print(l_line_num)
                print(l_line)
                print(e_line_num)
                print(e_line)
                print()

#def n_gram_score(e_source, l_source, score_limit):

syl_count('wordsworth #1.txt', 'latin.txt')
syl_count('wordsworth #1.txt', 'latin wordsworth.txt')
# syl_score('wordsworth #1.txt', 'latin.txt', 5)
syl_score('wordsworth #1.txt', 'latin wordsworth.txt', 5)