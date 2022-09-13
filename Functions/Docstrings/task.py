def increment_list(mylist):
    """This function adds 1 to each element of the list"""

    for i in range(len(mylist)):
        mylist[i] += 1

    return mylist

r=[]
n=int(input("Enter List Range: "))
for i in range(n):
    r.append(i+1)
print(r)
print(increment_list.__doc__)
print(increment_list(r))
