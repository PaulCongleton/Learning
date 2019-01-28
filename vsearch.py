def search4letters(phrase:str, letters:str='aeiou') -> set:
    #returns letters found in a string
    return set(letters).intersection(set(phrase))

def search4vowels(phrase:str) -> set:
    #returns vowels
    return set('aeiou').intersecion(set(phrase))
