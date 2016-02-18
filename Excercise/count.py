def count(sequence, item):
    found = 0
    for i in sequence:
        if i == item:
            found+=1
    return found
    
print count([1,23,45,5,5,5,5],5)
