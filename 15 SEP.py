#3-4-5
l=[ ]
for i in range (11):
           if i%2==0:
               l.append(i)
print(l)
print(sum(l))
l2=[]
import numpy as np
for i in range (0,11,2):                  #(ofc there's shorter and easier way for it ,I DON KNOW^.^)
           l2.append(i)
l2.remove(0)
print(np.prod(l2))
#------------------------------------------------------------------------------
#6-7
d={}
key=['a','b','c','d']
l=[1,2,3,4]
c=zip(key,l)
for key,l in c:
    d[key]=l
print(d)
#------
d2={}
key=['a','b','c','d']
l=[1,2,3,4]
l.reverse()
c=zip(key,l)
for key,l in c:
    d2[key]=l
print(d2)
#------------------------------------------------------------------------------