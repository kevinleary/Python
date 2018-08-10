import turtle

#t_left = turtle.Turtle()
#t_right = turtle.Turtle()
t = turtle.Turtle()

#1A
def binary_tree(depth, length):
    """This function is supposed to return a Binary Tree with depth six
        It its drawing opposite on other levels
    """
    a = 60

    if depth <= 0: 
                 # base case
        return   

    t.left(a)
    t.forward(length)
    t.right(a)
    binary_tree(depth-1, 0.6*length)
    t.left(a) 
    t.penup()
    t.backward(length)
    t.pendown()

    t.right(a)
    t.forward(length)
    t.left(a)
    t.right(a)
    binary_tree(depth-1, 0.6*length)
    t.penup()
    t.backward(length)
    t.pendown()
    #t.right(a) 
    #t.forward(length)
    return

#1B
def power_linear(x,n):
    """Uses a divide and conquer approach to compute powers
        where x is any number and n is a non negative integer
        so in the form X^n
    """
    try:
        if n == 0:          #base case
            return 1

        if n == 1:          #case if power = n which is X for all n
            return x

        if n%2 == 0:
            return power_linear(x, n/2) * power_linear(x, n/2)
    
        else:       #if its odd it will substract 1 then divide and continue
            return x * power_linear(x, (n-1)/2) * power_linear(x, (n-1)/2) 
    except ValueError:
        print("Entered a wrong value for X or N")


def test_power():
    """Tests the cases of power_linear using testif()

    """
    testname = "test power_linear()"
    b = 0

    if power_linear(1, 0) == 1:
        if power_linear(7, 1) == 7:
            if power_linear(2, 7) == 128:
                b = 1

    return testif(b, testname)

#1C
def slice_sum(lst, begin, end):
    """Adds the elements of lst from 0 to end-1
    
    """
    try:
        if begin == end:
            return 0
        else:
            return lst[begin] + slice_sum(lst, begin+1, end)
    except IndexError:
        print("Error due to begin and end incompatibility")
        

def test_slice_sum():
    """Tests the slice_sum function for correctness
    
    """
    test_name = "test_slice_sum"
    lst = [1,2,3,4,5,6,7,8,9,10]
    b = 0
    if slice_sum(lst, 0, 4) == int(sum(lst[0:4])):
        if slice_sum(lst, 1, 6) == int(sum(lst[1:6])):
            if slice_sum(lst, 5, 10) == int(sum(lst[5:10])):
                if slice_sum(lst, 7, 8) == int(sum(lst[7:8])):
                    b = 1
    return testif(b, test_name)


def slice_sum_m(lst, begin, end):
    """Adds the elements of lst from 0 to end-1 using memoization
    
    """
    sum_dict = {}
    try:
        if begin == end:
            return 0
        else:
            value = lst[begin] + slice_sum(lst, begin+1, end)
        sum_dict = value
        return sum_dict        
    except IndexError:
        print("Error due to begin and end incompatibility")    


def test_slice_sum_m():
    """Tests the slice_sum_m function for correctness.
    
    """
    test_name = "test_slice_sum_m"
    lst = [1,2,3,4,5,6,7,8,9,10]
    b = 0
    if slice_sum_m(lst, 0, 4) == int(sum(lst[0:4])):
        if slice_sum_m(lst, 1, 6) == int(sum(lst[1:6])):
            if slice_sum_m(lst, 5, 10) == int(sum(lst[5:10])):
                if slice_sum_m(lst, 7, 8) == int(sum(lst[7:8])):
                    b = 1
    return testif(b, test_name)


#testif ----------
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing power_linear(x,n)
        param b: boolean, normallya  tested condition
        param testname: the test name
        param msgOK: string to be printed if b ==True 
        param msgFailed: string to be printed if param b ==False
        returns b
    """
    if b:
        print("Sucess: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b



#a = 120
# turn to get started
#t.penup()

#t.left(-120)
#t_right.right(60)
#t.pendown()


#1A - test
#t.right(120)
#binary_tree(6,160)

#1B - test 
#test_power()

#1C - test
test_slice_sum_m()
test_slice_sum()


