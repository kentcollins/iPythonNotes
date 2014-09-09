init = '                              *                              '

def check(n):
    if n == '   ':
        return ' '
    elif n == '  *':
        return '*'
    elif n == ' * ':
        return ' '
    elif n == ' **':
        return ' '
    elif n == '*  ':
        return '*'
    elif n == '* *':
        return ' '
    elif n =='** ':
        return ' '
    elif n == '***':
        return ' '

def process(state):
    next = state[0]
    for pos in range(1, len(init)-1):
        next += check(state[pos-1:pos+2])    
    next+=state[len(state)-1]
    return next
    
gen = init
for i in range(20):
    print gen
    gen = process(gen)

    
    