#calculator.py

def sum(m, n):
    if (n>0):
        for i in range(0,n):
            m += 1
    else:
        for i in range(0,abs(n)):
            m -= 1
    return m
        

def divide(m, n):
    i = 0
    isNegative = m>0 and n<0 or m<0 and n>0
    m = abs(m)
    n = abs(n)
    
    while(m>=n):
        m -= n
        i += 1
    i = -i if isNegative else i
    
    return i