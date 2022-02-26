vowels = ['a', 'e', 'i', 'o', 'u']

word = "Milliways"
# word = input("Provive a word to search for vowels")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] = + 1

for i, v in sorted(found.items()):
    print(i, "was found", v, "time(s)")
