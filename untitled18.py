# ** 8 ** #

n=int(input("number of figurs u want:"))
l=[] 
for i in range(n):
    e=input("enter number{}:".format(i+1))
    l.append(e)
print(l)   
D={}

def a():
    D={x:l.count(x) for x in l}
    print(D)
    return
    a()
a()
# ------------------------------------------------------------------------------
# ** 9 ** #

lnumber= []
n = int(input(" enter number of elements for list : "))
for i in range(n):
    num = int(input(" now enter numbers: "))
    lnumber.append(num)
   




class Calc:
    def even(self, numbers):
        e=0
        o=0
        for num in numbers:
            if num % 2 == 0:
                e=num+e
            else:
                o=o+1
        result = {"even_sum": e , "odd_count": o}
        print(result)
calc = Calc()
 
calc.even(lnumber)





    

    
    
    
    
    