#Track the containers movement
def tracker():
    for e in range(0, len(j)):
        if j[e] == 'A':
            b = a[0]
            c = a[1]
            a[1] = b
            a[0] = c
        elif j[e] == 'B':
            b = a[1]
            c = a[2]
            a[2] = b
            a[1] = c
        elif j[e] == 'C':
            b = a[0]
            c = a[2]
            a[2] = b
            a[0] = c
#Check the final position
def check():
    if a[0] == 1:
        print("1")
    if a[1] == 1:
        print("2")
    if a[2] == 1:
        print("3")
#Initial position
a=[1,0,0]
#Input for the A,B, and C
j=input()
#Turn the input characters into capital characters
j=j.upper()
tracker()
check()