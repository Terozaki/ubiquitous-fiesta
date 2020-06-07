import math

running = True

#Functions

    #Basic Calculation Function

def calc(x,y,s):
    if s == 'add':
        return x + y
    if s == 'sub':
        return x - y
    if s == 'mul':
        return x * y
    if s == 'div':
        return x / y

    #Lowest Common Multiple Function

def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

    #Finds 'd' in completed square form

def complete_square_d(a,b,c):
    d = float(b / (2 * a))
    return d

    #Finds 'e' in completed square form

def complete_square_e(a,b,c):
    e = float(c - ((b * b) / (4 * a)))
    return e

    #Swaps inputted number's sign

def swap(x):
    y = x * -1
    return y

    #Finds the value of y, in a simultaneous equation

def solve_y(first_x, first_y, first_known, second_x, second_y, second_known):
    if first_y > second_y:
        first_greater = True
    else:
        first_greater = False

    if first_x == second_x:
        if first_greater:
            third_y = float(first_y - second_y)
            third_known = float(first_known - second_known)
            
        if not first_greater:
            third_y = float(second_y - first_y)
            third_known = float(second_known - first_known)
            
        value_y = float(third_known / third_y)
        return value_y

    else:
        multiplied_first_y = float(second_x * first_y)
        multiplied_second_y = float(first_x * second_y)
        multiplied_first_known = float(second_x * first_known)
        multiplied_second_known = float(first_x * second_known)

        if multiplied_first_y > multiplied_second_y:
            third_y = float(multiplied_first_y - multiplied_second_y)
            third_known = float(multiplied_first_known - multiplied_second_known)

        else:
            third_y = float(multiplied_second_y - multiplied_first_y)
            third_known = float(multiplied_second_known - multiplied_first_known)

        value_y = float(third_known / third_y)
        return value_y

    # #Finds the value of x, in a simultaneous equation

def solve_x(first_x, first_y, first_known, value_y):
    value_x = float((first_known - (value_y * first_y)) / first_x)
    return value_x

#Main Loop

while running:

    #Opening Screen
    print('Version 1.7.8')
    print('This is a calculator')
    print('By Anwen Brookes-Tee\n')
    print('Please enter the value of the calculation you wish to perform\n')
    print('1: Basic Calculation')
    print('2: Simultaneous Equations')
    print('3: Quadratic Graphs')
    print('4: Trigonometry\n')

    calculation = input('Enter Numerical Value: ')

    #Basic Calculations

    if calculation == '1':
        print('Choose a type of Basic Calculation\n')
        print('1: Addition')
        print('2: Subtraction')
        print('3: Multiplication')
        print('4: Division\n')

        basic_calculation = input('Enter Numerical Value: ')

        #Addition

        if basic_calculation == '1':
            sign = 'add'
            
        #Subtraction
            
        elif basic_calculation == '2':
            sign = 'sub'

        #Multiplication
        
        elif basic_calculation == '3':
            sign = 'mul'
            
        #Division

        elif basic_calculation == '4': 
            sign = 'div'

        #Error Checking
        
        else:
            print('That is not a recognised value.')

        #Calculation os Basic Values
            
        operand_1 = float(input('Operand 1: '))
        operand_2 = float(input('Operand 2: '))

        answer = calc(operand_1,operand_2,sign)
        print('The answer is', answer)

    #Simultaneous Equations

    elif calculation == '2':
        print('Choose the number of unknown values:\n')
        print('1: 2 Unknown Values')
        print('2: 3 Unknown values')
        print('3: 4 Unknown Values\n')

        values = input('Enter Numerical Value: ')

        #2 Unknown Values

        if values == '1':
            print('Choose the type of simultaneous equation input\n')
            print('1: ax + by = c')
            print('   dx + ey = f\n')
            print('2: by = ax + c')
            print('   ey = dx + f\n')
            value = input('Enter Numerical Value: ')

            #Takes values in ax + by = c form

            if value == '1':
                print('First Equation:')
                print('ax + by = c')
                
                first_x = float(input('a: '))
                first_y = float(input('b: '))
                first_known = float(input('c: '))
              
                print('Second Equation:')
                print('dx + ey = f')
                
                second_x = float(input('d: '))
                second_y = float(input('e: '))
                second_known = float(input('f: '))

            #Takes values in y = mx + c form
                
            if value == '2':
                print('First Equation:')
                print('by = ax + c')
                
                first_y = float(input('b: '))
                first_x = float( -1 * (float(input('a: ')) / first_y ))
                first_known = (float(input('c: ')) / first_y)

                print('Second Equation:')
                print('ey = dx + f')
                
                second_y = float(input('e: '))
                second_x = float( -1 * (float(input('d: ')) / first_y ))
                second_known = (float(input('f: ')) / first_y)

            #Calculates the values of x and y

            value_y = solve_y(first_x, first_y, first_known, second_x, second_y, second_known)
            value_x = solve_x(first_x, first_y, first_known, value_y)

            #Returns values of x and y 

            print('x =', value_x)
            print('y =', value_y)
            
        #3 Unknown Values

        elif values == '2':
            print('Sorry, this feature does not exist yet.')

        #4 Unknown Values
            
        elif values == '3':
            print('Sorry, this feature does not exist yet.')

        #Error handling
            
        else:
            print('That is not a recognised value.')

    #Complete The Square & Quadratic Graphs

    elif calculation == '3':
        print('Input the values of the letters in the equation')
        print('ax^2 + bx + c')
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))

        square_d = complete_square_d(a,b,c)
        square_e = complete_square_e(a,b,c)

        print('Choose Answer\n')
        print('1: Complete the Square')
        print('2: Calculate Roots')
        print('3: Calculate Turning Point\n')

        quad_answer = input('Enter Numerical Value: ')

        #Returns the Completed Square Form

        if quad_answer == '1':  
            print(a,'* ( x +', square_d, ')^2 +', square_e)

        #Returns the Roots of the Equation

        elif quad_answer == '2':
            if square_e <= 0:
                swapped_e = swap(square_e)
                swapped_d = swap(square_d)

                if math.sqrt(swapped_e) % 1 == 0:
                    pos_x = swapped_d + math.sqrt(swapped_e)
                    neg_x = swapped_d - math.sqrt(swapped_e)
                    print('x =', pos_x)
                    print('or')
                    print('x =', neg_x)

                elif math.sqrt(swapped_e) % 1 != 0:
                    print('x =', swapped_d, '+ √', swapped_e)
                    print('or')
                    print('x =', swapped_d, '- √', swapped_e)

                #Error Handling

                else:
                    print('Invalid Input')
            
            if square_e > 0:
                print('The roots cannot be calculated')

            else:
                print('That is not a valid input')

        elif quad_answer == '3':
            x_coord = swap(square_d)
            print('(',x_coord,',',square_e, ')')

        #Error Handling

        else:
            print('That is not a recognised value')

    #Calculate Basic Trigonometry

    elif calculation == '4':
        print('Choose the value of the unknown side\n')
        print('1: Opposite')
        print('2: Adjacent')
        print('3: Hypotenuse\n')

        value = input('Enter Numerical Value: ')

        angle = float(input('Enter angle: '))
        radians = math.radians(angle)

        #Calculate Opposite

        if value == '1':
            hypotenuse = float(input('Enter Hypotenuse: '))
            opposite = float(math.sin(radians) * hypotenuse)
            print('The Opposite is', opposite)

        #Calculate Adjacent
        
        elif value == '2':
            opposite = float(input('Enter Opposite: '))
            adjacent = float(opposite / math.tan(radians))
            print('The Adjacent is', adjacent)

        #Calculate Hypotenuse 

        elif value == '3':
            adjacent = float(input('Enter Adjacent: '))
            hypotenuse = float(adjacent / math.cos(radians))
            print('The Hypotenuse is', hypotenuse)

        #Error Handling

        else:
            print('That is not a valid input')

    #Error Handling

    else:
        print('That is not a recognised value')

    #Kill Program
    
    kill = input('Would you like to quit? ') == 'yes'
    if kill:
        running = False
    print('\n')
while not running:
    raise SystemExit
