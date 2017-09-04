def firstNotRepeatingCharacter(s):
    repeat = list()
    first_time = list()
    for i in s:
        if i not in first_time:
            first_time.append(i)
        else:
            repeat.append(i)
    for j in s:
        if j in first_time and j not in repeat:
            return j
    return "_"
        
    
    
            

