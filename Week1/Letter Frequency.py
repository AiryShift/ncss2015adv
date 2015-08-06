from collections import Counter
from string import ascii_lowercase
freq = Counter(input('Enter some text: ').lower())
for k, v in freq.items():
  if k in ascii_lowercase:
    print(k, v)
