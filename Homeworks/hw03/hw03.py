######################
# Required Questions #
######################

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    oof = 1
    while k > 0:
        oof = oof * n
        n = n -1
        k = k -1
    return oof


def nonzero(lst):
    """ Returns the first nonzero element of a list

    >>> nonzero([1, 2, 3])
    1
    >>> nonzero([0, 1, 2])
    1
    >>> nonzero([0, 0, 0, 0, 0, 0, 5, 0, 6])
    5
    """
    n = 0
    while lst[n] == 0:
        n = n + 1
    return lst[n]    


def has_n(lst, n):
    """ Returns whether or not a list contains the value n.

    >>> has_n([1, 2, 2], 2)
    True
    >>> has_n([0, 1, 2], 3)
    False
    >>> has_n([], 5)
    False
    """
    for x in lst:
        if x==n:
            return True
    return False


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    carrie_is_cool = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
            carrie_is_cool += 1
        else:
            n = n * 3 + 1
            print(n)
            carrie_is_cool += 1
    return carrie_is_cool
    

def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    if x % 2 == 0:
        return 'even'
    else: return 'odd'

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    return [odd_even(x) for x in s]


def decode_helper(pair):
    """
    Optional helper function! Could be useful to turn something like [0, 0] to 'Male 0-9'
    """
    # gender = "Male"
    one_age = -10
    two_age = -1

    if pair[0]==0:
        gender = "Male"
    else:
        gender = "Female"

    if pair [1] == 10:
        return gender + " 100+"

    for x in range(10):
        one_age += 10
        two_age += 10
        if pair[1] == x:
            break;


        # if n=1:
        #     one_age += n * 10

        
    return gender + " " + str(one_age) + "-" + str(two_age)
    

def decode(list_of_sex_age_pairs):
    """
    >>> decode([[0, 0], [1, 1], [1, 10]])
    ['Male 0-9', 'Female 10-19', 'Female 100+']
    >>> decode([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
    ['Male 0-9', 'Male 10-19', 'Male 20-29', 'Male 30-39', 'Male 40-49', 'Female 50-59', 'Female 60-69', 'Female 70-79', 'Female 80-89', 'Female 90-99', 'Female 100+']
    """ 
    return [decode_helper(x) for x in list_of_sex_age_pairs]
    

