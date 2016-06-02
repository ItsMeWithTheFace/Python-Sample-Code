# Rakin Uddin

def radix_sort(l, ind=-1):
    '''(list of ints) -> list of ints
    Takes an unordered list of integers and returns the list with the integers
    sorted from smallest to largest

    >>> radix_sort([1, 3, 2])
    [1, 2, 3]
    >>> radix_sort([4, 2, 4, 5, 70, 1])
    [1, 2, 4, 4, 5, 7]
    >>> radix_sort([])
    []
    '''
    # Putting the list of ints into a main container as a copy of l
    main_bin = l[:]
    # Initialize a list of digit bins
    bins = [[],[],[],[],[],[],[],[],[],[]]

    # Go through list and consider the first digit in each element and add the
    # whole number to the corresponding digit bin
    for i in range(len(main_bin)):
        removed_val = main_bin.pop(0)
        # If the digit placeholder we're looking at does not exist for the curr
        # value, then treat it as a 0 i.e., 05, 06, etc
        if(ind >= -(len(str(removed_val)))):
            bins[int(str(removed_val)[ind])].append(removed_val)
        # Otherwise the digit placeholder does exist and we treat that digit as
        # the index to put the value in
        elif(ind < -(len(str(removed_val)))):
            bins[0].append(removed_val)

    # General Case:
    # Go through each digit bin in order and remove all contents, putting them
    # back into the main bin, then sort the new main bin again

    # Base Case:
    # First check if the length of the 0 digit bin is equal to the length of
    # the original list, then all the values have been sorted
    if(len(bins[0]) == len(l)):
        main_bin = bins[0]
        return main_bin
    # Recursive Decomposition:
    # Else proceed with general case
    else:
        for dig_bin in bins:
            for j in range(len(dig_bin)):
                popped_val = dig_bin.pop(0)
                main_bin.append(popped_val)
        # lowering the index by 1 to check the next digit spots
        return radix_sort(main_bin, ind-1)
