
#version 1.0:  finding a perfect cube root of an interger
# solution: exhaustive enumeration

# x = int(raw_input("x= "))
# ans = 0
# counting = 0
#
# while ans**3 < abs(x):
#    ans += 1
#    counting += 1
# print "counting = ",counting
#
# if ans**3 != abs(x):
#    print "can't find the cube root of x."
# elif x < 0:
#    print "the cube root of x is: ", -ans
# else:
#    print "the cube root of x is: ", ans
#
#version2.0: finding the approximate cube root of a float number
# solution: exhaustive enumeration
#
# x = float(raw_input("x = "))
# ans = 0.0
# counting = 0
# epsilon = 0.1
# step = 0.001
#
# while( abs(ans**3 - abs(x)) > epsilon and ans < abs(x)):
#    ans += step
#    counting += 1
# print "counting = ", counting
#
# if ans >= abs(x):
#    print "can't find the cube root of x."
# elif x < 0.0:
#    print "the cube root of x is:",-ans
# else:
#    print  "the cube root of x is:",ans

# test 1:
# x = 125
# counting =  4999
# the cube root of x is: 4.999
# Ques1: how can be more accurate? it satisfies the requirement, though.
#
# test 2:
# x = 12345
# counting =  12345000
# can't find the cube root of x.
# Ques2: what is the affecting factor? Update to version 2.1
#
# test 3:
# x = -987
# counting =  987001
# can't find the cube root of x.
#
# test 4:
# x = -1000
# counting =  10000
# the cube root of x is: -10.0


#version2.1: finding a approximate cube root of a float number
# solution: exhaustive enumeration
# try to solve the problem of Ques2 in Version2.0.

# x = float(raw_input("x = "))
# ans = 0.0
# counting = 0
# epsilon = 0.1
# step = 0.0001
#
# while( abs(ans**3 - abs(x)) > epsilon and ans < abs(x)):
#    ans += step
#    counting += 1
# print "counting = ", counting
#
# if ans >= abs(x):
#    print "can't find the cube root of x."
# elif x < 0.0:
#    print "the cube root of x is:",-ans
# else:
#    print  "the cube root of x is:",ans

#change step to 0.0001
# test 1:
# x = -987
# counting =  99562
# the cube root of x is: -9.95619999999
#
# test 2:
# x = 12345
# counting =  231116
# the cube root of x is: 23.1116
#
# test 3:
# x = 111111111111
# ^Z
# [1]+  Stopped
# Ques3: Performance problem. Need to improve the algorithm (change solution)

# test 4 :a number of tests: x < 1 or x < epsilon
# Ques4: WHAT is the pattern?  Ans may be bigger than x. Update to version 3.0
# x = 0.999
# counting =  9652
# the cube root of x is: 0.9652
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.001
# counting =  0
# the cube root of x is: 0.0
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.005
# counting =  0
# the cube root of x is: 0.0
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.11
# counting =  1100
# can't find the cube root of x.
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.12
# counting =  1200
# can't find the cube root of x.
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.09
# counting =  0
# the cube root of x is: 0.0
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.2
# counting =  2001
# can't find the cube root of x.
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.9
# counting =  9001
# can't find the cube root of x.
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.99
# counting =  9620
# the cube root of x is: 0.962
# taideMacBook-Air:Documents taixiaomei$ python test.py
# x = 0.91
# counting =  9101
# can't find the cube root of x.


# version3.0: finding a approximate cube root of a float number
# solution: exhaustive enumeration
# try to solve the problem of Ques4 in version 2.1.
# sometimes ans is bigger than abs(x)
#
# x = float(raw_input("x = "))
# ans = 0.0
# counting = 0
# epsilon = 0.1
# step = 0.0001
#
# if x <= 1.0:
#    termination = 1.0
# else:
#    termination = abs(x)
#
# while( abs(ans**3 - abs(x)) > epsilon and ans <= termination):
#        ans += step
#        counting += 1
#
# print "counting = ", counting
#
# if  abs(ans**3 - abs(x)) > epsilon:
#    print "can't find the cube root of x."
# elif x < 0.0:
#    print "the cube root of x is:",-ans
# else:
#    print  "the cube root of x is:",ans


# Now, there are 3 questions:
# test 1: within epsilon range, fnding the most approximate cube root
# x = 1.0
# counting =  9655
# the cube root of x is: 0.9655
#
# test 2: when x is less than epsilon, the ans is 0
# x = 0.008
# counting =  0
# the cube root of x is: 0.0
#
# test 3: improvement of algorithm for super large input x
# x = 12345678
# ^Z
# [4]+  Stopped                 python test.py



#version4.0: finding the most approximate cube root of a float number
# solution: exhaustive enumeration
# try to solve the problem of Ques4 in version 3.0.

# x = float(raw_input("x = "))
# ans = 0.0
# counting = 0
# epsilon = 0.1
# step = 0.0001
#
# if abs(x) <= 1.0:
#    termination = 1.0
# else:
#    termination = abs(x)
#
#
# while( abs(ans**3 - abs(x)) > epsilon and ans < termination):
#        ans += step
#        counting += 1
#
#
# if  abs(ans**3 - abs(x)) > epsilon:
#    print "can't find the cube root of x."
# else:
#    while abs(ans**3 - abs(x)) > abs((ans+step)**3 - abs(x)):
#        ans = ans + step
#        counting += 1
#    if x < 0.0:
#       # ans = -ans
#    print "the cube root of x is:",ans
#
#
# print "counting = ", counting
#
#

#version5.0: finding the most approximate cube root of a float number
# solution: bi-section searching
# try to solve the problem of test 3 in version 3.0.

#x = float(raw_input("x = "))


# import traceback
# import sys
# try:
    # x = float(raw_input("x = "))
# except:
    # traceback.print_exc()
    # #sys.exc_info()
    # raise

# if x > 99999999999999999999.0 or x < -99999999999999999999.0:
    # raise ValueError('Invalid value of x')

# counting = 0
# epsilon = 0.1
# step = 0.0001
# starting = 0.0

# if abs(x) <= 1.0:
    # termination = 1.0
# else:
    # termination = abs(x)


# ans = (starting + termination)/2

# #while abs(ans**3 - abs(x)) > epsilon and ans < termination:
# while abs(ans**3 - abs(x)) > epsilon:  #will this loop terminate?
    # if ans**3 > abs(x):
        # termination = ans
    # else:
        # starting = ans
    # ans = (starting + termination)/2
    # counting += 1
   # # print counting
   # # print starting, termination, ans

# if  abs(ans**3 - abs(x)) > epsilon:
    # print "can't find the cube root of x."
# else:
    # while abs(ans**3 - abs(x)) > abs((ans+step)**3 - abs(x)):
        # ans = ans + step
        # counting += 1
    # while abs(ans**3 - abs(x)) > abs((ans-step)**3 - abs(x)):
        # ans = ans - step
        # counting += 1

    # if x < 0.0:
        # ans = -ans
    # print "the cube root of x is:",ans


# print "counting = ", counting




# test 1:
# x = 12345678
# the cube root of x is: 231.120418163
# counting =  41
# Although the problem of large number is solved (performance), accuracy is decreased:
# test 2:
# x = 125
# the cube root of x is: 4.99996811523
# counting =  25

#version6.0: finding the most approximate cube root of a float number
# solution: bi-section searching
# code optimization
#
#import traceback
#import sys
#try:
#    x = float(raw_input("x = "))
#except:
#    traceback.print_exc()
#    raise
#if x > 99999999999999999999.0 or x < -99999999999999999999.0:
#    raise ValueError('Invalid value of x')
#
#counting = 0
#epsilon = 0.1
#step = 0.0001
#starting = 0.0
#termination = max(1.0, abs(x))
#ans = (starting + termination)/2
#
##while abs(ans**3 - abs(x)) > epsilon and ans < termination:
#while abs(ans**3 - abs(x)) > epsilon:  #will this loop terminate?
#    if ans**3 > abs(x):
#        termination = ans
#    else:
#        starting = ans
#    ans = (starting + termination)/2
#    counting += 1
#
#if  abs(ans**3 - abs(x)) > epsilon:
#    print "can't find the cube root of x."
#else:
#    while abs(ans**3 - abs(x)) > abs((ans+step)**3 - abs(x)):
#        ans = ans + step
#        counting += 1
#    while abs(ans**3 - abs(x)) > abs((ans-step)**3 - abs(x)):
#        ans = ans - step
#        counting += 1
#
#    if x < 0.0:
#        ans = -ans
#    print "the cube root of x is:",ans
#print "counting = ", counting


#version7.0: finding the most approximate cube root of a float number
# solution: bi-section searching
# code optimization: assertion, decomposition and abstraction into functions


def ave(a,b):
    """ a, b are floats
    returning their averages """
    return (a+b)/2

def input():
    # Ques: diff between eval() and float()?
    x = eval(raw_input("x = "))
    #Ques: how to limit range of X?
    assert x > -9.9E+20 and x < 9.9E+20
    print locals()
    return x

epsilon = 0.1
step = 0.0001

while True:
    counting = 0
    x = input() 
    starting = 0.0
    termination = max(1.0, abs(x))
    ans = ave(starting, termination)
    
    #while abs(ans**3 - abs(x)) > epsilon and ans < termination:
    while abs(ans**3 - abs(x)) > epsilon:  #will this loop terminate?
        if ans**3 > abs(x):
            termination = ans
        else:
            starting = ans
        ans = ave (starting, termination)
        counting += 1

    if  abs(ans**3 - abs(x)) > epsilon:
        print "can't find the cube root of x."
    else:
        while abs(ans**3 - abs(x)) > abs((ans+step)**3 - abs(x)):
            ans = ans + step
            counting += 1
        while abs(ans**3 - abs(x)) > abs((ans-step)**3 - abs(x)):
            ans = ans - step
            counting += 1

        if x < 0.0:
            ans = -ans
        print "the cube root of x is:",ans
    print "counting = ", counting
