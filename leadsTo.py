def leadsTo(s, delta):
    result = set()

    for x in delta:
        if x[1] == s:
            result.add(x[2])

    return result
