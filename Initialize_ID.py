# Before you make fun of this code, it was a direct line=by-line port from a PHP version.
# The goal was to make it perform exactly as the PHP without changing the logic; so called 'port refactoring'.

import re

inputFileName = '_disambiguator_input.csv'

outf1 = open('_attribute_line','wt')
outf2 = open('_attribute_metric','wt')

inputFile = open(inputFileName,'rt')
patno = []

for line in inputFile:
    patno.append(line.split('\t')[4])
inputFile.close()

inputFile = open(inputFileName, 'rt')
inventors = {}
inventor_id = []
inventors_start = []
inv = ''
start = 0

n = 0
while n < len(patno)-1:
    while n < len(patno)+1:
        if (n == len(patno)) or (patno[start] != patno[n]):
            end = n-1
            inv = inv.strip()
            inventors[start] = inv
            inv = ''
            start = n
            if n < len(patno):
                n -= 1
            else:
                break
        else:
            inventors_start.append(start)
            inventor_id.append(patno[n] + '-' + str(n-start+1))
            line = inputFile.readline()
            linex = line.split('\t')
            invx = linex[1] + ' ' + linex[2] + ' ' + linex[3]
            invx = re.sub('[\t\r\n]', ' ', invx)
            invx = re.sub('[ ]+', '_', invx)
            invx = invx.strip()
            inv = inv + invx + ' '
        n += 1

inputFile.close()

inputFile = open(inputFileName, 'rt')

n = 0
for line in inputFile:
    line = line.replace('\n', '')
    line = line.split('\t')
    name = line[1] + ' ' + line[2] + ' ' + line[3]
    name = re.sub('[\t\r\n]', ' ', name)
    name = re.sub('[ ]+', '_', name)
    assignee = line[11]
    assignee = re.sub('[\t\r\n]', ' ', assignee)

    out2 = "{}\t0\t{}\t{}\t{}\t{}\t{}".format(line[4],name,assignee,line[5],line[3],inventor_id[n])
    out2 = out2.strip()
    out2 = out2.upper()
    outf2.write(out2 + '\n')

    class_id = line[5]
    class_id = class_id.lower()

    lastname = re.sub('[\t\r\n]', ' ', line[3])
    lastname = re.sub('[ ]+', '_', lastname)
    lastname = lastname.lower()
    assignee = re.sub('[\t\r\n]', ' ', line[11])
    assignee = re.sub('[ ]+', '_', assignee)
    assignee = assignee.lower()
    city = re.sub('[\t\r\n]', ' ', line[7])
    city = re.sub('[ ]+', '_', city)
    city = city.lower()

    name = name.lower()

    if len(name) > 0:
        firstname_letter = name[:1]
    else:
        firstname_letter = ''

    if (len(assignee) > 0) and (assignee != '|'):
        out1 = "FN{} LN{} NM{} AS{} CT{} CL{}".format(firstname_letter,lastname,name,assignee,city,class_id)
    else:
        out1 = "FN{} LN{} NM{} AS CT{} CL{}".format(firstname_letter,lastname,name,city,class_id)

    out1 = re.sub('[ ]+', ' ', out1)
    out1 = out1.strip()
    outf1.write(out1 + '\n')

    n += 1

inputFile.close()
outf1.close()
outf2.close()