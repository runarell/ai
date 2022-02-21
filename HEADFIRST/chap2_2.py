vowels = ['a', 'e', 'i', 'o', 'u']

word = "Milliways"
# word = input("Provive a word to search for vowels")

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)

print(found)
