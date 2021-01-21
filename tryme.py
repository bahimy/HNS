#! /usr/bin/python3

source = ""
data = list()
blankFlag = False

with open("qsource") as f:
    source = f.read()

for i, l in enumerate(source.splitlines()):

    if i > 20: # remove enumeration from the final script
        break

    if l.find('№') > -1:
        data.append([])

    else:

        if not l:

            blankFlag = True

        else:

            if blankFlag:
                data[len(data) - 1].append(l)
                data[len(data) - 1].append(list())
            else:
                data[len(data) - 1][len(data[len(data) - 1]) - 1].append(l)

            blankFlag = False

print(data);
