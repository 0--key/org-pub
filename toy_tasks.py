def detect_number(word):
    for letter in word:
        try:
            #
            order = int(letter)
            return (word, order)
        except ValueError:
            continue


def order(string):
    mixed_string_words = []
    for word in string.split():
        mixed_string_words.append(detect_number(word))
    pure_words = []
    for i in sorted(mixed_string_words, key=lambda x: x[1]):
        #print(i, i[0])
        pure_words.append(i[0])
    return ' '.join(pure_words)


#print(order("is2 Thi1s T4est 3a"))
#assert(order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est")
# Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")


# Description:

# You get an array of arrays.
# If you sort the arrays by their length, you will see, that their length-values are consecutive.
# But one array is missing!


# You have to write a method, that return the length of the missing array.

# Example:
# [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3


# If the array of arrays is null/nil or empty, the method should return 0.

# When an array in the array is null or empty, the method should return 0 too!
# There will always be a missing element and its length will be always between the given arrays.

def get_length_of_missing_array(array_of_arrays):
    if array_of_arrays == []:
        return 0
    elif len(array_of_arrays) == 1:
        return array_of_arrays[0]
    else:
        array_of_lenght = sorted([len(x) for x in array_of_arrays])
        sattelite = [x for x in range(array_of_lenght[0],
                                      len(array_of_lenght)+2)]
        mix = array_of_lenght + sattelite
        missed_length = mix.pop(0)
        #if mix:
        for i in mix:
            missed_length = i ^ missed_length
        return missed_length


#print(get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
assert(get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]) == 3)

# You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at that index and insert it back to another place in the number.

# Doing so, find the smallest number you can get.

# Task:

# Return an array or a tuple depending on the language (see "Your Test Cases" Haskell) with
# 1) the smallest number you got
# 2) the index i of the digit d you took, i as small as possible
# 3) the index j (as small as possible) where you insert this digit d to have the smallest number.
# Example:

# smallest(261235) --> [126235, 2, 0]
# 126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

# smallest(209917) --> [29917, 0, 1]

# [29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than
# index `i` in [29917, 0, 1].
# 29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the number 29917.

# smallest(1000000) --> [1, 0, 6]

def smallest(n):
    """Seems like exchange the largest number in the greater digits
    with a smallest one in a minors"""
    nl = [int(x) for x in str(n)]
    nl.reverse()
    smallest_index = len(nl) - nl.index(min(nl)) - 1
    nl.reverse()
    smallest_item = nl[smallest_index]
    for i in nl:
        if smallest_item < i:
            replacement = nl.index(i)
            break
    nl[smallest_index] = i
    nl[replacement] = smallest_item
    result = int(''.join(str(letter) for letter in nl))
    return [result, smallest_index, replacement]

# print(smallest(209917))
# print(smallest(1000000))
# print(smallest(162235))


# Common denominators

# You will have a list of rationals in the form

#  [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
#  where all numbers are positive ints.

#  You have to produce a result in the form

#   [ [N_1, D] ... [N_n, D] ]
#   in which D is as small as possible and

#    N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
#    Example :

#     [ [1, 2], [1, 3], [1, 4] ] produces the array [ [6,12], [4,12], [3,12] ]

def convertFracts(lst):
    list_of_denominators = [x[1] for x in lst]
    # sift this list and remove out the largest values
    list_of_denominators.sort(reverse=True)
    for i in range(len(list_of_denominators)):
        for j in range(i+1, len(list_of_denominators)):
            if list_of_denominators[i] % list_of_denominators[j] == 0:
                list_of_denominators.pop(j)
                break
    # find the minimal possible denominator
    min_denom = 1
    for i in list_of_denominators:
        min_denom *= i
    # convert the initial array in proportion with min_denom
    for i in range(len(lst)):
        # print(lst[i])
        lst[i][0] = int(lst[i][0] * min_denom / lst[i][1])
        lst[i][1] = min_denom
    return lst

print(convertFracts([ [1, 2], [1, 3], [1, 4] ]))
