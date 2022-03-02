def search4vowels(phrase:str) -> str :
    """Return any vowels found in an asked-for word.""" # 함수 밑의 docstring은 help(함수)를 했을 때 나온다.
    vowels = set('aeiou')
    return vowels.intersection(set(phrase)) # set.intersetion(set) : 두 set자료에 대해서 교집합을 return

def search4letters(phrase:str, letter:str) -> str :
    """Return a set of the 'letters' found in 'phrase'.""" # docstring의 들여쓰기를 틀리면 error가 나오기때문에 주의
    return set(letter).intersection(set(phrase))
