## Data Abstraction ##

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]

from math import sqrt
def distance(city_1, city_2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    """

    "*** YOUR CODE HERE ***"
    return sqrt((((get_lat(city_1)-get_lat(city_2))**2) + ((get_lon(city_1)-get_lon(city_2))**2)))
    

def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    place = make_city('place', lat, lon)
    if distance(place, city1) < distance(place, city2):
        return city1[0]
    return city2[0]


## Dictionaries

def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    "*** YOUR CODE HERE ***"
    dictionary = {}
    for words in word_list:
        dictionary[words] = message.count(words)
    return dictionary



def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> e = replace_all(d, 3, 'poof')

    >>> e == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for i in d:
        if d[i] == x:
            d[i] = y
    return d



def make_politician(name, party, age):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> isinstance(woodrow, dict)
    True
    """
    # Make sure you use a dictionary in your implementation!
    "*** YOUR CODE HERE ***"
    pol = {'name': name , 'party': party, 'age': age}
    return pol
    

def get_pol_name(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_pol_name(woodrow)
    'Woodrow Wilson'
    """
    "*** YOUR CODE HERE ***"
    return politician['name']
    

def get_party(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_party(woodrow)
    'Democrat'
    """
    "*** YOUR CODE HERE ***"
    return politician['party']

def get_age(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_age(woodrow)
    57
    """
    "*** YOUR CODE HERE ***"
    return politician['age']
    

