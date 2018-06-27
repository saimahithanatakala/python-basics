#while loop
acc_num=12345
num=int(input("enter the acc_num"))
while acc_num!=num:
    print("wrong number")
    num=input("enter the correct acc_num")
print("welcome to your account")



#while true and break statement
sum=0
while True:
    data=int(input("enter the data"))
    if data==0:
        break
    sum=sum+data
print("sum is ",sum)
