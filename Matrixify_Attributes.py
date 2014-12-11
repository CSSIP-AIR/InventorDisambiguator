# Ported from Matrixify_attribute.php but leaving all the multi-threading and recombining of files stuff behind.

import os
import collections

def generate_newsdict(infn, outfn):
    inf = open(infn, 'rt')
    outf = open(outfn, 'wt')

    dict = []

    for content in inf:
        content = content.replace('\n', '')
        words = content.split(' ')
        for word in words:
            if word not in dict:
                dict.append(word)

    inf.close()

    for i in range(0, len(dict)):
        outf.write(str(i+1) + '\t' + dict[i] + '\t1\n')

    return dict

def generate_newspara(infn, outfn, dict):
    inf = open(infn, 'rt')
    outf = open(outfn, 'wt')

    n = 0
    for line in inf:
        line = line.replace('\n', '')
        words = line.split(' ')
        lineCounter = collections.Counter(words)
        for word in words:
            outf.write(str(n+1) + ',' + str(dict.index(word)+1) + ',' + str(lineCounter[word]) + '\n')
        n += 1




dict = generate_newsdict('_attribute_line', '_attribute_dictionary')

generate_newspara('_attribute_line', '_attribute_matrix', dict)

