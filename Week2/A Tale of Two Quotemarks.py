import re

with open('atotc.txt') as f:
    for line in f:
        for match in re.findall(r'".*?"', line.strip()):
            print(match[1:-1])
