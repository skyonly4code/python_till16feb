n=int(input("enter the number "))
r=n%10
r= r in [0,1,2,8,9]
out='divisble'*r + 'not divisible'*(1-r)
print(out)
