# Rakin Uddin 

def edit_distance(s1, s2):
    '''(str, str) -> int
    Returns the minimum number of single-character changes that would be needed
    to turn s1 into s2

    >>> edit_distance('hello', 'helll')
    1

    >>> edit_distance('13SEAHOrse', '45seahorse')
    7

    REQ: s1 and s2 must be the same length
    REQ: only character changes available are replacing one character with
    another
    '''
    # Base Case: When the length of the strings are 1(or 0), check if their
    # chars are the same. If they are, add 0 to changes required else add 1
    if(len(s2) == 0):
        result = 0

    if(len(s2) == 1):
        if(s2[0] == s1[0]):
            result = 0
        else:
            result = 1
    # N-1 Case: Repeat the base case, but check the rest of the string while
    # repeating the checking conditions
    else:
        if(s2[0] == s1[0]):
            result = 0 + edit_distance(s1[1:], s2[1:])
        else:
            result = 1 + edit_distance(s1[1:], s2[1:])
    # Return result
    return result


def subsequence(s1, s2):
    '''(str, str) -> bool
    Returns True iff s1 is a subsequence of s2. s1 is a subsequence of s2 if s2
    can be equal to s1 by having 0 or more of its chars removed

    >>>subsequence(’dog’,’XYZdABCo123g!!!’)
    True

    >>>subsequence(’doge’,’XYZdABCo123g!!!’)
    False

    REQ: len(s2) >= len(s1)
    '''
    # Base Case: when both s1 and s2 have only one value, compare those values
    # and the result is True or False
    if(len(s1) == 1 and len(s2) == 1):
        if(s1[0] == s2[0]):
            result = True
        else:
            result = False
    # N-1 Case: when a character is found in s2 that equals current char in s1,
    # look at the rest of both lists
    else:
        if(s2[0] == s1[0]):
            result = subsequence(s1[1:], s2[1:])
        # Else keep looking at current char in s1, but look at rest of s2
        else:
            result = subsequence(s1, s2[1:])
    # Return the result
    return result


def perms(s):
    '''(str) -> set of str
    Returns a set of all the possible permutations of s

    >>> perms('ab')
    {'ab', 'ba'}

    >>> perms('1dc')
    {'1dc', 'd1c', 'dc1', '1cd', 'c1d', 'cd1'}
    '''
    # Base Case: If there is only one letter in the str, it is the only
    # permutation
    if(len(s) == 1):
        result = s[0]
    # N-1 Case
    else:
        # Get the permutations of the rest of the list
        next_perm = perms(s[1:])
        result = []
        # Look through each permutation of the list
        for perm in next_perm:
            # For each permutation, put the first char of s in every possible
            # spot in the permutation, then do the same with the next perms
            for i in range(len(perm) + 1):
                result.append(perm[:i] + s[0] + perm[i:])
    # Return the list as a set
    return set(result)
