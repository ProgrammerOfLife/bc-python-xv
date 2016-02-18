def factorial(num):
    li = range(1,num+1)
    cal = reduce(lambda x,y: x*y, li)
    return cal

