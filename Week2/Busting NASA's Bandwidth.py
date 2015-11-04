import re
PATTERNS = [
    re.compile(r'\[0[1-9]/Jul/1995'),  # Date check
    # Image directiory, HTTP, response code
    re.compile(r'"GET /images/.*HTTP/1.0" 200'),
    # Extensions
    re.compile(r'GET /images/.*\.(gif|png|jpg|jpeg) ', re.IGNORECASE)
]
min_size = int(input('Minimum response size: '))


def check(l):
    for pattern in PATTERNS:
        if not re.search(pattern, l):
            return False
    return True


with open('access.log') as f:
    valids = [line.strip() for line in f if check(line)]

validSizes = [i for i in filter(lambda x: x >= min_size, [
    int(re.search(r'200 (.*)$', i).group(1)) for i in valids])]
print('# requests: {}'.format(len(validSizes)))
print('# bytes: {}'.format(sum(validSizes)))
