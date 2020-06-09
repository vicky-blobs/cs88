"""Lab 2: Functions """

## Coding

def a_or_c(grade):
    """
    We all know the saying "C's get degrees".
    We all would like to get an A, but sometimes
    a C will have to do. 

    Return whether the grade inputted
    would receive an A or C.

    >>> a_or_c(100)
    True
    >>> a_or_c(75)
    True
    >>> a_or_c(82)
    False
    >>> a_or_c(80)
    False
    >>> a_or_c(95)
    True
    >>> a_or_c(40)
    False
    """
    if (grade >= 90):
        return True
    elif (grade >= 70 and grade<80):
        return True
    else: 
        return False


## Control

def min(x, y):
    """
    Return the minimum between x and y

    >>> min(1,2)
    1
    >>> min(3,1)
    1
    >>> min(2,3)
    2
    >>> min(0, 67777)
    0
    >>> min(-1, -5)
    -5
    >>> min(-7, -1)
    -7
    >>> min(0, 0)
    0
    """
    if x<y:
        return x
    else: 
        return y


## Transformation

def abs_value_equal(x, y):
    """Return whether or not the absolute value of both numbers is the same.

    Please refrain from using libraries (abs)

    >>> abs_value_equal(-2, -2)
    True
    >>> abs_value_equal(-3, 3)
    True
    >>> abs_value_equal(1, 2)
    False
    >>> abs_value_equal(3, 3)
    True
    >>> abs_value_equal(-6, -6)
    True
    >>> abs_value_equal(-1, -5)
    False
    >>> abs_value_equal(5, -6)
    False
    """
    if(x > 0) :
        x = x*-1
    if(y > 0) :
        y = y*-1
    return y == x


## Representation

def mirror(num1, num2):
    """
    Return if num1 is num2 backwards

    >>> mirror(121, 121)
    True
    >>> mirror(543, 345)
    True
    >>> mirror(343, 436)
    False
    >>> mirror(33, 33)
    True
    >>> mirror(42, 52)
    False
    >>> mirror(12, 22)
    False
    """
    reference = 0;
    new = 0;
    while(num1 > 0):
        new = num1 % 10
        reference = (reference * 10)+ new
        num1 = num1//10
    return num2 == reference




