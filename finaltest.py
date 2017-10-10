def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.     Count how manytimes letter appears in s1 and in s2, and ret    urn the bigger of the twocounts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max (s1.count(letter), s2.count(letter))



def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the       letters in prefix.
    '''
    return s1.startswith(prefix) and s2.startswith(prefix)


def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
   ['a', 'c', 'e', 'g', 'i']
   '''

    result = []
    i = 0
    while i < len(L):
       result.append(L[i])
       i = i+n
   
    return result


def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    ['a', 1]
    '''

    result = []
    for k in d:
        if k in L:
            result.append(k)

    return result


def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
       if L1[i] != len(L2[i]):
            result = False

    return result

def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
             if L[row][col] < 0:
                neg.append(L[row][col])
             else:
                nonneg.append(L[row][col])
    return (neg, nonneg)



def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        d[c] = d[c]+1  ## Does Not work
