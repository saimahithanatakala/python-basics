#list containing tuples
a=[('a',4),('b',6),('c',8),('d',2)]    #sort according to second element
def fun(x):
    return x[1];
a.sort(key=fun)
print(a)

