MAX_COUNT = 10000


# number shuold be a positive integer?
def cube_int(number):
    """input a positive integer
    return 0 if not being able to find"""
    if number == 0:
        return 0
    if number == 1:
        return 1

    min_number = 0
    max_number = number

    value = number // 2
    count = 0

    while True:
        count += 1
        real_number = value ** 3
        if real_number > number:
            max_number = value
        elif real_number < number:
            min_nmber = value
        else:
            break
        
        value = (min_number + max_number) // 2
        
        print "(min_number = ", min_number, " max_number = ", max_number, " value = ", value, " )"
        print count
        
        value = (min_number + max_number) // 2
        if value == min_number or count > MAX_COUNT:
            value = 0
            break

    return value



ACCURACY = 0.0001

def cube_float(number):
    min_number = 0
    max_number = number

    value = number/2
    count = 0

    while True:
        count += 1
        real_number = value ** 3
        if real_number > number + ACCURACY:
            max_number = value
            print "real_number > number + ACCURACY, real_number = ", real_number
        elif real_number < number - ACCURACY:
            min_number = value
            print "real_number < number - ACCURACY, real_number = ", real_number

        else:
            print "break"
            break
            
        value = (min_number + max_number)/2
        print "(min_number = ", min_number, " max_number = ", max_number, " value = ", value, " )"
        print count
        if value <= min_number + ACCURACY or count > MAX_COUNT:
            print "min_number + ACCURACY = ",min_number+ACCURACY
            value = 0
            break
    return value

def cube():
    try:
        while True:
            x = eval(raw_input("please input the value = "))
            neg_flag = False


            if x < 0:
                neg_flag = True
                x = abs(x)

            if isinstance(x, int):
                value = cube_int(x)
            else:
                value = cube_float(x)

            if neg_flag:
                value = -1 * value

            if x == 0:
                print("Value is 0")
            elif value == 0:
                print("cannot find the cube")
            else:
                print("value is  ", str(value))
    except:
        print("input error, please input int or float")

cube()


