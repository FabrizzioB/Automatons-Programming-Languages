def symbolsIn(word, sep="_"):
    result = []
    new_word = word

    if word.find(sep):
        result = new_word.split(sep)
        return result

    if sep == "":
        for x in word:
            result.append(x)

        return result

    if word == sep:
        result.append("")
        result.append("")
        return result