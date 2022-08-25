import random

f = open("donhurtme.txt", "r")

a = f.readline()
a = a[35:199+35]

print("ptitctf{" + a + "}")
mylist = []

for i in range(len(a)):
    g = (i, a[i])
    mylist.append(g)
random.shuffle(mylist)

#print(*mylist)

for c in (mylist):
    print("flag[" + str(c[0])+"] = \""+str(c[1])+"\"")
