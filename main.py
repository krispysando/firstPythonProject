words = ["abc", "def", "ghi", "jkl"]
goodWords = [""]
goodLetters = ["b", "h"]
badLetters = ["e", "f"]
i = 0

for word in words:
    if goodLetters[i] in word:
        print("yes " + word)
        goodWords.extend(word)
        i += 1

print(goodWords)
