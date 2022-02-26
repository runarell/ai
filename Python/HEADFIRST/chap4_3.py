def sear4vowels(phrase: str) -> set:
    '''Return any vowels found in a supplied word.'''
    vowels = set("aeiou")
    return vowels.intersection(set(phrase))


def sear4letters(phrase: str, letters: str) -> set:
    ''' Return a set of thr "letters" found in "phrase" '''
    return set(letters).intersection(set(phrase))

# print(sear4vowels("hitch_hiker"))


print(sear4letters("hitch_hiker", "aeiou"))
