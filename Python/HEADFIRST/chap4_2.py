

def sear4vowels(word: str) -> set:
    '''Return any vowels found in a supplied word.'''
    vowels = set("aeiou")
    return vowels.intersection(set(word))


print(sear4vowels("hitch_hiker"))
