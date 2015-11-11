with open('elements.txt') as f:
    ELEMENTS = set(i.split(',')[1] for i in f)


def validate(compound):
    return False

line = input('Line: ')
while line:
    if validate(line):
        print('Valid.')
    else:
        print('Invalid.')
    line = input('Line: ')
