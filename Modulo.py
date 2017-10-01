#Input function
def run():
    for a in range(0,10):
        b=int(input())
        h.append(b)
#Run modulo 42 function
def modulo():
    for d in h:
        e = d % 42
        c.append(e)
#initial empty containers
h=[]
c=[]
run()
modulo()
total=len(set(c))
print(total)
