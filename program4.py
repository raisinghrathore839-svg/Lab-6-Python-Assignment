words = ['apple', 'ant', 'banana', 'ball', 'cat']

grouped = {}

for word in words:
    first = word[0]

    if first in grouped:
        grouped[first].append(word)
    else:
        grouped[first] = [word]

print(grouped)
