#Reverse polish notion calculator


opf = {'*': lambda x,y: x*y,
       '+': lambda x,y: x+y,
       '-': lambda x,y: y-x,
       '/': lambda x,y: x/y}


def rpn(expr):
    tokens = expr.split(' ')
    stack = []

    while tokens:
        token = tokens.pop(0)

        if token.isdigit():
            stack.append(token)
        else:
            stack.append(opf[token](int(stack.pop()),int(stack.pop())))

    return stack[0]
    

assert(rpn("5 2 +") == 7)
assert(rpn("6 2 * 3 +") == 15)
assert(rpn("5 1 2 + 4 * + 3 -") == 14)
