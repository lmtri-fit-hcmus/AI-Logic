# define class store literal
class Literal:
    def __init__(self, _isPos, _sign):
        self.isPos = _isPos
        self.sign = _sign

    def printLiter(self):
        str = ''
        if self.isPos == 0:
            str = str + ' -' + self.sign
        else:
            str = str + ' ' + self.sign
        return str

# split a line of input txt to list of literals.
def splitLiteral(literal):
    i = 0
    tmp = ''
    literal
    res = []
    while (i < len(literal)):
        if(literal[i] !=' '):
            tmp += literal[i]
        else:
            if (tmp != 'OR'):
                if tmp[0] == '-':
                    res.append(Literal(0, tmp[1]))
                else:
                    res.append(Literal(1, tmp[0]))
            tmp = ''
        i += 1
    if (tmp != 'OR'):
        if tmp[0] == '-':
            res.append(Literal(0, tmp[1]))
        else:
            res.append(Literal(1, tmp[0]))
    #print(res)
    return res


#Loop all line in input.txt and handle them
def handleInput(filename):
    listLiter = []
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    negaAlpha = splitLiteral(lines[0])
    for i in negaAlpha:
        if (i.isPos == 0):
            i.isPos = 1
        else:
            i.isPos = 0

    for i in range(2, len(lines)):
        listLiter.append(splitLiteral(lines[i]))

    return listLiter, negaAlpha
