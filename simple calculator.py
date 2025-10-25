while True:
    num_1 = float(input('Enter the first number: '))
    operator = input('Enter any operator (+, -, *, /) or q to quit')
    if operator.lower() == 'q' :
        print('Calculator exiting...')
        break

    num_2 = float(input('Enter the second number: '))

    


    if operator == '+':
        result = num_1 + num_2
    elif operator == '-' :
        result = num_1 - num_2
    elif operator == '*':
        result = num_1*num_2
    elif operator == '/':
        if num_2 != 0:
            result = num_1/num_2
        else:
            print('Cannot Divide by 0')
            continue
    else:
        print('Invalid Operator !')
        continue
    print('Result', result) 