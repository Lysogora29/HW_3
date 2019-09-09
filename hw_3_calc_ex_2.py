try:
    num_1 = input ('Enter numeric 1: ')
    num_1 = int(num_1)
    aref_oper = input ('Select +, -, *, /, %, **, : ')
    num_2 = input ('Enter numeric 2: ')
    num_2 = int(num_2)

    if aref_oper == '+':
        print ('result', num_1 + num_2)
    elif aref_oper == '-':
        print ('result', num_1 - num_2 )
    elif aref_oper == '*':
        print ('result', num_1 * num_2 )
    elif aref_oper == '**':
        print ('result', num_1 ** num_2 )
    elif aref_oper == '/':
        if num_2 != 0:
            print ('result', num_1 / num_2 )
        else:
            print ('division by zero')
    elif aref_oper == '%':
        if num_2 != 0:
            print ('result', num_1 % num_2 )
        else:
            print ('division by zero')
    else:
        print ('wrong operation sing')
except:
    print('Only numbers')
