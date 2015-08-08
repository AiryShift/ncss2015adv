def isAscending(line):
    line = line.split()
    if line != sorted(line) or len(line) != len(set(line)):
        return False
    return True

with open('lines.txt') as f:
    for lineNum, line in enumerate(f):
        if isAscending(line):
            print('Line {} is ascending.'.format(lineNum + 1))
