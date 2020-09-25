#program to find prime factors of given input number

n=input()
print("Prime Factors of "+n+" are:",end="")
for j in range(50):
    for i in range(3,int(n),2):

        #chacking divisiable by 2 or not
        while int(n)%2==0:
            n=int(n)/2
            print("2 ",end="")

        #chacking divsiable by any number 3 to ....
        if int(n)%i==0:
            n=int(n)/i
            print(i,end=" ")
            break

if not n==1:
    print(int(n))