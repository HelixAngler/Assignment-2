#Generate acronym
def acro():
    for g in a:
        print(g[0].upper(), end="")
#Name input(space must be replace with -)
name=input()
#Convert name into list array
a=name.split('-')
acro()