def sum_digits(num):
    sum=0
    while num>0:
        temp=num%10
        num//=10
        sum+=temp
    return sum    
     

num=int(input("enter the number: "))
print("the sum of the digits of the number is:",sum_digits(num))