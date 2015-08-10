with open('words.txt') as f:
    words = [word.strip() for word in f]

for word in sorted(words, key=lambda x: x[::-1]):
    print(word)
