#! /usr/bin/python3

import re

source = ""
data = list()
blankFlag = False

with open("qsource") as f:
    source = f.read()

for l in source.splitlines():

    # Strings with '№' sign shows the beginning of the new chapter
    if l.find('№') > -1:
        data.append([])

    else:

        if not l:
            blankFlag = True

        else:

            # Blank line preceding the one with content signifies the
            # beginning of the new block; blankFlag in false allows to
            # distinguish a question from the options.
            if blankFlag:
                data[len(data) - 1].append(
                        re.sub('^\s+\d+\.\s+', '', l).capitalize())
                data[len(data) - 1].append(list())
            else:
                data[len(data) - 1][len(data[len(data) - 1]) - 1].append(
                        re.sub('^\s+\d+\.\s+', '', l))

            blankFlag = False

print(data);
