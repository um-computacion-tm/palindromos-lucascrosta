#funcioniterativa
def palindromeit(pal):

    pal = pal.lower()

    pal2 = pal[::-1]

    if pal == pal2:

        return True
    
    else:

        return False
    

#funcionrecursiva
def palindromerec(pal):

    pal = pal.lower()

    if len(pal) <= 1:
        return True

    if pal[0] == pal[-1]:
        return palindromerec(pal[1:-1])
    else:
        return False





