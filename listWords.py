import re

def listWords(fileName):
    result = []

    str = open(fileName, "r").read()

    new_str = re.sub(u'[^a-zA-Z0-9àáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', ' ', str)

    result = new_str.lower().split()

    return result