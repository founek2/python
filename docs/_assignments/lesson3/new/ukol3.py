def is_descending():
    ...


assert is_descending([3, 4]) == False
assert is_descending([5, 5]) == False
assert is_descending([10, 1]) == True
assert is_descending([10, 8, 7, 6, 1, -10, -20]) == True
assert is_descending([10, 8, 7, 6, 6, 1, -10, -20]) == False
assert is_descending([1]) == True


values = []


def add_and_increase():
    """
    first argument append to values, then increase every value in list by value of second argument
    """
    ...


assert add_and_increase(3, 1) == [4]
assert add_and_increase(10, 3) == [7, 13]
assert add_and_increase(2, -1) == [6, 12, 1]
