from engsyllabifier import *
from latinsyllabifier import *
from collections import Counter
from eng_latin_generalizer import *

def listOlists_combiner(listOlists):
    i = 0
    output = []
    while i < len(listOlists):
        output = output+listOlists[i]
        i += 1
    return output

    if len(listOlists) == 0:
        return []
    else:
        print(listOlists[0])
        return listOlists[0]+listOlists_combiner(listOlists[1:])
    listOlists[z-1]+listOlists[z] + []

def l_syl_counter(source):
    count = 0

    with open(source, 'r') as file:
        latin  = file.read()

    l_syllables = syllabifier(latin)

    for line in l_syllables:
        for syl in line:
            count += 1
    return count

def e_syl_counter(source):
    count = 0

    with open(source, 'r') as file:
        english  = file.read()

    e_syllables = e_syllabifier(english)

    for line in e_syllables:
        for syl in line:
            count += 1
    return count

def line_counter(source):
    count = 0

    with open(source, 'r') as file:
        passage = file.read()

    syllables = e_syllabifier(passage)

    for line in syllables:
        count += 1
    return count

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

    # print("Pre-generalized:")
    # all_l = listOlists_combiner(l_syllables)
    # print("Syllables and their Occurences in: " + l_source)
    # print(Counter(all_l).most_common(25))
    # all_e = listOlists_combiner(e_syllables)
    # print("Syllables and their Occurences in: " + e_source)
    # print(Counter(all_e).most_common(25))
    # print()

    print("Generalized:")
    all_l = listOlists_combiner(gen_l_syllables)
    print("Syllables and their Occurences in: " + l_source)
    print(Counter(all_l).most_common(25))
    all_e = listOlists_combiner(gen_e_syllables)
    print("Syllables and their Occurences in: " + e_source)
    print(Counter(all_e).most_common(25))
    print()

def eng_corpus_syl_count(sources):
    count = 0
    gen_syllables = []

    for source in sources:
        with open(source, 'r') as file:
            passage_temp = file.read()

        syllables = e_syllabifier(passage_temp)
        for line in syllables:
            gen_syl = []
            for syl in line:
                count += 1
                x = generalize_eng(syl)
                gen_syl.append(x)
            gen_syllables.append(gen_syl)

    all_syls = listOlists_combiner(gen_syllables)
    print("Syllables and their Occurences in the translation corpus is:")
    print(Counter(all_syls).most_common(25))
    print()


def syl_score(e_source, l_source, score_limit):
    gen_e_syllables = []
    gen_l_syllables = []
    hits = 0
    l_syls = l_syl_counter(l_source)
    e_syls = e_syl_counter(e_source)
    l_lines = line_counter(l_source)
    e_lines = line_counter(e_source)

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
                hits += 1
                # print(score)
                # print(l_line_num)
                # print(l_line)
                # print(e_line_num)
                # print(e_line)
                # print()
    print("Sources:")
    print(e_source)
    print(l_source)
    print("Cutoff score of:")
    print(score_limit)
    print("line-to-line phonetic references are:")
    print(hits)
    print("Number of lines in Latin and English passages:")
    print(l_lines)
    print(e_lines)
    print("The fraction of phonetic references to total lines in the english passage is:")
    print(hits/e_lines)
    print()

def score_tester(a, b, c, d, e, lat):
    i = 6
    while i > 3:
        syl_score(a, lat, i)
        syl_score(b, lat, i)
        syl_score(c, lat, i)
        syl_score(d, lat, i)
        syl_score(e, lat, i)
        i -= 1

syl_score('Mackail.txt', 'latin.txt',5)
eng_corpus_syl_count(['wordsworth #1.txt','dryden.txt', 'Morris.txt', 'Mackail.txt', 'Fairfax Taylor.txt'])
syl_count('wordsworth #1.txt', 'latin.txt')
syl_count('dryden.txt', 'latin.txt')
syl_count('Morris.txt', 'latin.txt')
syl_count('Mackail.txt', 'latin.txt')
syl_count('Fairfax Taylor.txt', 'latin.txt')
score_tester('wordsworth #1.txt', 'dryden.txt', 'Morris.txt', 'Mackail.txt', 'Fairfax Taylor.txt', 'latin.txt')
