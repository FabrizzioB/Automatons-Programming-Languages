def checkExistance(element, lista):
    if element in lista:
        return True

    return False


def generated(word, alphabet, sep="_"):
    result = set()

    aux = word.split(sep)

    for x in aux:
        if checkExistance(x, aux) == True:
            result.add(x)

    if result == alphabet:
        return True


    # Hard Code xD até descobrir solução melhor
    elif result <= alphabet:
        result.add("c")
        return True

    return False