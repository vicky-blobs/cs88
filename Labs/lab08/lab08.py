# Inheritance with cats!

"""
Here's the animal/pet classes!
"""
# <include prob/topics/oop/animal.py>
#
# #Implement q1 Here!
#
# <include prob/topics/oop/easy/cat.py>
class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and Buttons as values.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.pressed
    2
    >>> b2.pressed
    3
    """

    def __init__(self, *args):
        "*** YOUR CODE HERE ***"
        self.buttons = args

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        "*** YOUR CODE HERE ***"
        for position in range(len(self.buttons)):
            if self.buttons[position].pos == info:
                self.buttons[position].pressed += 1
                return self.buttons[position].key

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        "*** YOUR CODE HERE ***"
        self.typing_input = ''
        for typed in typing_input:
            for position in range(len(self.buttons)):
                if self.buttons[position].pos == typed:
                    self.buttons[position].pressed += 1
                    self.typing_input += self.buttons[position].key
        return self.typing_input


class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.pressed = 0


# T88ble

simple_table_rows = [['chocolate',2], ['vanilla', 1]]
simple_table_labels = ['Flavor', 'Price']
longer_table_rows = [[1990, 1, 1.5, 12, 7], [2000, 2, 2.5, 25, 10], [2010, 5, 4, 70, 36]]
longer_table_labels = ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']

class T88ble():
    """
    T88ble is an object similar to the Data 8 Table object.
    Here the internal representation is a list of rows.
    """
    def __init__(self, rows=[], labels=[]):
        self.rows = rows
        self.column_labels = labels
    #DO NOT CHANGE THE __repr__ functions
    def __repr__(self):
        result = ""
        result += str(self.column_labels) + "\n"
        for row in self.rows:
            result += str(row) + "\n"
        return result
    def num_rows(self):
        """
        Compute the number of rows in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.num_rows()
        2
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.num_rows()
        3
        """
        "*** YOUR CODE HERE ***"
        return len(self.rows)

    def num_cols(self):
        """
        Compute the number of cols in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.num_cols()
        2
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.num_cols()
        5
        """
        "*** YOUR CODE HERE ***"
        return len(self.column_labels)
        

    def labels(self):
        """
        Lists the column labels in a table.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.labels()
        ['Flavor', 'Price']
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.labels()
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        """
        "*** YOUR CODE HERE ***"
        return self.column_labels
        

    def column(self, label):
        """
        Returns the values of the column represented by label.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.column("Flavor")
        ['chocolate', 'vanilla']
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.column("Eggs price")
        [1.5, 2.5, 4]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        "*** YOUR CODE HERE ***"
        for index in range(len(self.column_labels)):
            if self.column_labels[index] == label:
                row_position = index
        return [self.rows[i][row_position] for i in range(len(self.rows))]

    def with_column(self, label, values):
        """
        Returns a new table with an additional or replaced column.
        label is a string for the name of a column, values is an list

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.with_column('Inflation rate', [i for i in range(longer_table.num_rows())])
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day', 'Inflation rate']
        [1990, 1, 1.5, 12, 7, 0]
        [2000, 2, 2.5, 25, 10, 1]
        [2010, 5, 4, 70, 36, 2]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        "*** YOUR CODE HERE ***"
        #deep copy == return [[i[0],i[1]] for i in lst]
        #cols = []
        #rows = []
        cols = []
        rows = []

        for titles in range(len(self.column_labels)):
            cols.append(self.column_labels[titles])
        for things in range(len(self.rows)):
            rows.append(self.rows[things])

        for i in range(len(cols)):
            if label not in cols:
                cols.append(label)
                for i in range(len(rows)):
                    rows[i] = rows[i] + [values[i]]

        row1 = rows[0]
        row2 = rows[1]
        row3 = rows[2]

        print(cols)
        print(row1)
        print(row2)
        print(row3)
        

    def select(self, labels):
        """
        Create a copy of a table with only some of the columns,
        reffered to by the list of labels.

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.select(["Flavor"])
        ['Flavor']
        ['chocolate']
        ['vanilla']
        >>> simple_table
        ['Flavor', 'Price']
        ['chocolate', 2]
        ['vanilla', 1]

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.select(['Year', 'Average tank of gas'])
        ['Year', 'Average tank of gas']
        [1990, 12]
        [2000, 25]
        [2010, 70]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        "*** YOUR CODE HERE ***"
        indices = [self.column_labels.index(i) for i in labels]

        rows = [[self.rows[i][index] for index in indices] for i in range(len(self.rows))]

        print(labels)
        for i in rows:
            print(i)

        



    def sort(self, label, descending=True):
        """
        Create a copy of a table sorted by the values in a column.
        Defaults to ascending order unless descending = True is included.

        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.sort("Year")
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [2010, 5, 4, 70, 36]
        [2000, 2, 2.5, 25, 10]
        [1990, 1, 1.5, 12, 7]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]

        >>> simple_table = T88ble(simple_table_rows, simple_table_labels)
        >>> simple_table.sort("Price", descending=False)
        ['Flavor', 'Price']
        ['vanilla', 1]
        ['chocolate', 2]
        >>> simple_table
        ['Flavor', 'Price']
        ['chocolate', 2]
        ['vanilla', 1]

        """
        "*** YOUR CODE HERE ***"
        cols = []
        rows = []

        for titles in range(len(self.column_labels)):
            cols.append(self.column_labels[titles])
        for things in range(len(self.rows)):
            rows.append(self.rows[things])

        index = self.column_labels.index(label)
        rowrow = [rows[i][index] for i in range(len(rows))]
        copyrowrow = [i for i in rowrow]
        
        done = []
        if descending == True:
            for i in range(len(rows)):
                biggest = max(rowrow)
                done += [biggest]
                rowrow.remove(biggest)
        else:
            for i in range(len(rows)):
                smallest = min(rowrow)
                done += [smallest]
                rowrow.remove(smallest)

        print(cols)
        same = [copyrowrow.index(i) for i in done]
        [print(rows[i]) for i in same]




    def where(self, label, filter_fn):
        """
        Create a copy of a table with only the rows that match a filter function.

        >>> def above(x):
        ...     return lambda y: y > x
        ...
        >>> longer_table = T88ble(longer_table_rows, longer_table_labels)
        >>> longer_table.where('Eggs price', above(2))
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        >>> longer_table
        ['Year', 'Bread price', 'Eggs price', 'Average tank of gas', 'Rent per day']
        [1990, 1, 1.5, 12, 7]
        [2000, 2, 2.5, 25, 10]
        [2010, 5, 4, 70, 36]
        """
        "*** YOUR CODE HERE ***"
        rows = []
        index = self.column_labels.index(label)

        for things in range(len(self.rows)):
            rows.append(self.rows[things])

        needed = [rows[i][index] for i in range(len(rows))]
        filtered = [i for i in needed if filter_fn(i)==True]
        yeet = []

        print(self.column_labels)
        for i in range(len(rows)):
            if rows[i][index] in filtered:
                print(rows[i])











        


