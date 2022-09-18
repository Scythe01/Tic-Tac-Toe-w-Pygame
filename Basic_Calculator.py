#Basic Calculator
print('\n_________________________\n|\tOPERATIONS\t|\n|\'+\' = Addition\t\t|\n|\'-\' = Subtraction\t|\n|\'x\' = Multiplication\t|\n|\'/\' = Division\t\t|\n|\'%\' = Remainder\t|\n|\'^\' = Exponentiation\t|\n|\'<\' = Less than\t|\n|\'>\' = Greater than\t|\n|\'=\' = Equal\t\t|\n|_______________________|')
while True:
    user = input('\n------------------------------------------------------------\nChoose an operation or quit [ + | - | x | / | % | ^ | < | > | = ]: ').lower()
    if user == '+' or user == '+ ' or user == ' + ' or user == ' +' or user == '-' or user == '- ' or user == ' - ' or user == ' -' or user == 'x' or user == 'x '  or user == ' x ' or user == ' x' or user == '/' or user == '/ ' or user == ' / ' or user == ' /' or user == '% ' or user == '%' or user == ' % ' or user == ' %' or user == '^' or user == '^ ' or user == ' ^ ' or user == ' ^' or user == '<' or user == '< ' or user == ' < ' or user == ' <' or user == '>' or user == '> ' or user == ' > ' or user == ' >' or user == '=' or user == '= ' or user == ' = ' or user == ' =' or user == 'quit' or user == 'quit '  or user == ' quit ' or user == ' quit' or user == 'q ' or user == 'q'  or user == ' q ' or user == ' q':
        while True:
            try:
                if user == 'quit' or user == 'quit '  or user == ' quit ' or user == ' quit' or user == 'q ' or user == 'q'  or user == ' q ' or user == ' q':
                    quit()
                number1 = float(input('Enter first number: '))
                number2 = float(input('Enter second number: '))
                if user == '+' or user == '+ ' or user == ' + ' or user == ' +':
                    print(f'{number1} + {number2} =', number1 + number2)
                elif user == '-' or user == '- ' or user == ' - ' or user == ' -':
                    print(f'{number1} - {number2} =', number1 - number2)
                elif user == 'x' or user == 'x ' or user == ' x ' or user == ' x':
                    print(f'{number1} × {number2} =', number1 * number2)
                elif user == '/' or user == '/ ' or user == ' / ' or user == ' /':
                    print(f'{number1} ÷ {number2} =', number1 / number2)
                elif user == '%' or user == '% ' or user == ' % ' or user == ' %':
                    print(f'{number1} % {number2} =', number1 % number2)
                elif user == '^' or user == '^ ' or user == ' ^ ' or user == ' ^':
                    print(f'{number1}^{number2} =', number1 ** number2)
                elif user == '<' or user == '< ' or user == ' < ' or user == ' <':
                    print(f'{number1} < {number2} =', number1 < number2)
                elif user == '>' or user == '> ' or user == ' > ' or user == ' >':
                    print(f'{number1} > {number2} =', number1 > number2)
                elif user == '=' or user == '= ' or user == ' = ' or user == ' =':
                    print(f'{number1} == {number2} =', number1 == number2)
                break
            except ValueError:
                print('Please type a valid number!')
    else:
        print('Please type a valid answer!')
    continue