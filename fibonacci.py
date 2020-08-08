n = int( input ("enter the no.of integer to be in fibonacci series: " ))
i=0
f=0
s=1
t=0
print("0")
print("1")
while i<n-2:
    
    t=f+s
    f=s
    s=t
    print(t)
    i += 1
