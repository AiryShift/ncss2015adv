def isAscending(line):
  line = line.split()
  if line != sorted(line) or len(line) != len(set(line)):
    return False
  return True

with open('lines.txt') as f:
  lineNum = 1
  for line in f:
    # print('Checking line {}'.format(line))
    if isAscending(line):
      print('Line {} is ascending.'.format(lineNum))
    lineNum += 1
