#Build a faulty calculator which give wrong answer for particular value of 2 integers 

a = eval(input())
b = eval(input())
x = input("Choose any Mathematical Operator :  " )

if x == "*":
    if (a == 45)and(b == 3 ):
         print(555)
    else:
        print(a*b)
elif x == "+":
    if (a ==56)and(b == 9) :
      print(77)
    else :
        print(a+b)
elif x == "-":
    print(a-b)
elif x =="/":
    if (a == 56)and(b==6):
       print(4)
    else:
        print(a/b)
