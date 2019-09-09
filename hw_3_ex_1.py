try:

    a = int(input ('enter num 1 :'))
    b = int(input ('enter num 2 :'))
    c = int(input ('enter num 3 :'))

    num_max = 0
    num_min = 0


    if a>b and a>c:
        num_max = a
    elif b>a and b>c:
        num_max = b
    elif c>num_max:
        num_max = c
        if a<=b and a<=c:
            num_min = a
        elif b<=a and b<=c:
            num_min = b
        elif c<=num_min:
            num_min = c
        print('Max number:', num_max)
        print('Min number:', num_min)
    else:
        print(a, b, c)

# except Exception as e: #?
#     print (e)
except:
    print('Enter only natural numbers')
    
    


