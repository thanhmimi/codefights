def sumOfTwo(a, b, v):
    my_set = set(b)
    for i in a:
        if ((v-i) in my_set):
            return True
    return False
