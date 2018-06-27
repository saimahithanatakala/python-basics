"""if result should be in the form of list"""
def fib(n):
 result=[]
 a,b=0,1
 while a<n:
     result.append(a)
     a,b=b,a+b
 return result
f=fib(200)
print(f)
