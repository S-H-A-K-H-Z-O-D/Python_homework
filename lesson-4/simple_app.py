
while True:
    a = int(input('a = '))
    b = int(input('b = '))

    operation = input("Choose: (+, -, *, /)")
    if operation == '+':
        print('a + b =', a+b)
    elif operation == '-':
        print('a - b=', a - b)
    
    q = input("Dou you want to run again? ")
    if q.lower() in ['q', 'quit', 'n', 'no']:
        break

