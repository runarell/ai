
def sear4vowels(word):
    '''Display any vowels found in an asked-for word.'''
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

        # 주석
sear4vowels("hitch_hiker")
