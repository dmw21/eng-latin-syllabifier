import string
from syllable3 import generate
from latinsyllabifier import syllabifier, list_lister

with open('wordsworth #1.txt', 'r') as file:
    passage = file.read()

#normalize words
def e_worder(line):
    space = -1
    words = []
    while '-' in line:
        line = line.replace('-', ' ')
    line = line.lower().translate(str.maketrans('', '', string.punctuation)).\
        translate(str.maketrans('', '', string.digits)).strip()
    while '  ' in line:
        line = line.replace('  ', ' ')
    line += ' '
    for i in range(len(line)):
        if line[i] == ' ':
            words.append(line[space + 1:i])
            space = i
    return (words)

#break up lines
def e_liner(passage):
    enter = -1
    lines = []
    passage += '\n'
    for i in range(len(passage)):
        if passage[i] == '\n':
            lines.append(passage[enter + 1:i])
            enter = i
    return(lines)

#syllabify
def e_line_syllabifier(line):
    lineSyllables = []
    for word in e_worder(line):
        write = open('helper.txt', 'w')
        syllable_w = generate(word.rstrip())
        if syllable_w:
            for syll in syllable_w:
                for s in syll:
                    print(s, file=write)
        else:
            for syll in syllabifier(word):
                for s in syll:
                    print("*"+s, file=write)
        write.close()

        read = open("helper.txt", "r")
        lines = read.readlines()
        for temp in lines:
            while temp != "":
                if temp[0] != '*':
                    syllable = ''.join(i for i in temp if i.isupper())
                else:
                    syllable = temp[1:-1]
                lineSyllables.append(syllable)
                temp = read.read()
        read.close()
    return(lineSyllables)

#call sylabifier on lines
def e_syllabifier(passage):
    syllables = []
    for line in e_liner(passage):
        syllables.append(e_line_syllabifier(line))
    return syllables

#for numbers with syllabify
def e_syllabifier_line_numbers(passage):
    lines = e_syllabifier(passage)
    output = []
    lineNumber = 1
    for line in lines:
        output.append((lineNumber, line))
        lineNumber += 1
    return output

list_lister(e_syllabifier_line_numbers(passage))