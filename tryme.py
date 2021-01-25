#! /usr/bin/python3

import re
import random
import keys

source = ""         # Holds data source text
data = list()       # Data source as list
blankFlag = False   # Tracks continuous blank lines
done = {0}          # Tracks already asked questions

with open("qsource") as f:
    source = f.read()

for l in source.splitlines():

    # Strings with '№' sign shows the beginning of the new chapter (i)
    if l.find('№') > -1:
        data.append(list())

    else:

        if not l:
            blankFlag = True

        else:

            # Line with content with preceding blank one signifies the
            # beginning of the new block; blankFlag in false allows to
            # distinguish a question from the options.
            if blankFlag:

                # Appends section container (j)
                data[len(data) - 1].append(list())

                # Appends question
                data[len(data) - 1][len(data[len(data) - 1]) - 1].append(
                        re.sub('^\s+\d+\.\s+', '', l).capitalize())

                # Appends options container (k)
                data[len(data) - 1][len(data[len(data) - 1]) - 1].append(
                        list())

            else:
                # Appends options
                data[len(data) - 1][len(data[len(data) - 1]) - 1][1].append(
                        re.sub('^\s+\d+\.\s+', '', l))

            blankFlag = False


def countTotal():
    ''' Count total of possible questions

    Returns:
    total amount of possible questions as integer
    '''
    total = 0

    for i in range(len(data)):
        total += len(data[i])

    return total

def determineQuestionID():
    ''' Determines per session unique question ID

    Returns:
    Question ID as integer
    '''

    target = 0

    if countTotal() == len(done):
        done.clear()
        done.add(0)

    while target in done:
        target = random.randint(1, countTotal())

    done.add(target)

    return target

def queryUser(target):
    ''' Queries the user and reports if the answer is correct

    returns:
    index of right answer; -1 otherwise
    '''

    def getQuestion():
        ''' Form a question string out of random 'database' list entry

        Returns:
        string containing a question with a set of options
        delimitet by new line
        '''

        def drawLine(length):
            ''' Generates a line for decoration

            returns:
            a line of various length
            '''

            line = ''
            for i in range(int(length*0.75)):
                line += '-'

            return line


        tally = 0
        result = ''

        for i, di in enumerate(data):
            for j, dj in enumerate(data[i]):
                tally +=1
                if tally == target:
                    result += '\n{0}\n{1}\n'.format(data[i][j][0],
                            drawLine(len(data[i][j][0])))
                    for k, dk in enumerate(data[i][j][1]):
                        result += '{0}. {1}\n'.format(k+1, dk)

        return result

    def checkAnswer():
        ''' Checks user's answer and makes response

        Returns:
        string with textual description if the users answer war right or wrong
        '''
        tally = 0
        for i, di in enumerate(keys.keys):
            for j, dj in enumerate(keys.keys[i]):
                tally += 1
                if tally == target:
                    if keys.keys[i][j] == int(guess):
                        return 'Правильно'
                    else:
                        return 'Неправильно. Верный ответ {0}'.\
                                format(keys.keys[i][j])

    print(getQuestion())
    guess = input("Номер ответа: ")
    print(checkAnswer())

while True:
    queryUser(determineQuestionID())
