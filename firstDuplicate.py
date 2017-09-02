def firstDuplicate(a):
    my_set = set()
    for i in a:
        if i in my_set:
            return i 
        my_set.add(i)
    return -1
        
