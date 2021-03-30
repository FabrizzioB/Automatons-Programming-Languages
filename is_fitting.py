def is_symbol(x):
    return (isinstance(x,str)) and (len(x) > 0) and (' ' not in x)

def is_variable(x):
    return is_symbol(x) and x[0].isupper()

def is_terminal(x):
    return is_symbol(x) and not is_variable(x)

def is_word(x):
    return isinstance(x, list) and all(is_symbol(c) for c in x)

def is_state(x):
    return isinstance(x, int)

def is_transition(x):
    if len(x) == 5:
        (q0, a, s0, q1, s1) = x
        return is_state(q0) and is_state(q1) and (len(a) == 0 or is_word(a)) and is_word(s0) and is_word(s1)
    else:
        return False

def is_configuration(x):
    if len(x) == 3:
        (q, tape, stack) = x
        return is_state(q) and (is_word(tape) and all(is_terminal(c) for c in tape)) and is_word(stack)
    else:
        return False

def is_fitting(c, t):
    if is_configuration(c) and is_transition(t):
        (q, tape, stack) = c
        (q0, a, s0, q1, s1) = t
        s2 = stack[0:len(s0)]
        return (q0 == q) and (len(a) == 0 or tape[0] == a) and (s2 == s0)
    else:
        return False


print(is_variable('Fdqsds sdasd'))

w = [x for x in 'Adqwdjqousd']
print(w)
print(is_word(w))

#"""def is_grammar(x):
#	return isinstance(x, list) \
#		and all(is_rule(p) for p in x)"""

#Um simbolo e uma string nao vazia em que nao ocorre ' '
#Uma variavel e um simbolo que começa por uma letra maiuscula (ch.isupper())
#Um terminal e um simbolo que nao e uma variavel
#Uma palavra e uma lista de simbolos
#Um estado(de controlo de automato) e um inteiro
#A transicao ...
#A configuracao...
