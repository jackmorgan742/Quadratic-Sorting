# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L):
    '''
    locates and returns index where the value of 0 is at O(log(n))
    '''
    low = 0
    high = len(L) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If 0 is greater, ignore left half
        if L[mid] < 0:
            low = mid + 1
 
        # If 0 is smaller, ignore right half
        elif L[mid] > 0:
            high = mid - 1
 
        # means 0 is present at mid
        else:
            return mid
 
    # If we reach here, then 0 was not present
    return -1

def bubble(L, left, right):
    '''
    sorts the sub-list L[left:right] using bubble sort algorithm
    '''
    for i in range(right-left):
        for j in range(left, right-i-1):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp

def selection(L, left, right):
    '''
    sorts the sub-list L[left:right] using selection sort algorithm
    '''
    for i in range(right-left):
        max_indx = left
        swap = right-i-1
        for j in range(left, right-i):
            if L[j] > L[max_indx]:
                max_indx = j
        L[swap], L[max_indx] = L[max_indx], L[swap]

def insertion(L, left, right):
    '''
    sorts the sub-list L[left:right] using insertion sort algorithm
    '''
    for i in range(right-left):
        for j in range(right-i, right):
            if L[j-1]>L[j]:
                tmp = L[j]
                L[j] = L[j-1]
                L[j-1] = tmp

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half