import time
import random

def find(a,b):
    if b!=0:
        return find(b,a % b)
    else:
        return a
#print("最大公约数："+ str(find(50,70)))

def IsS(a):
    b = int(a**0.5)+1
    i=2
    while(i<=b):
        if(a % i==0):
            return False
        i=i+1
    return True

def FindMG(n):
    i=1
    while(i<=n):
        b=((2<<i)-1)
        if(IsS(b)):
            print("梅根数"+str(b))
        i=i+1

#t1=time.time()
#FindMG(20)
#t2=time.time()
#print("所需时间：" + str(t2-t1))

def _3X(n,i):
    print(n,i+1)
    if(n!=1):
        if(n%2==0):
            _3X(n>>1,i+1)
        else:
            _3X(3*n+1,i+1)
    else:
        return i
#_3X(10,0)

def GDBHCX(n):
    i=1
    while(i<n/2):
        if(IsS(i) and IsS(n-i)):
            print(str(n) + "=" + str(i) + "+" + str(n-i))
        i=i+1

#GDBHCX(90)

arr=[0 for i in range(29)]
#print(len(arr))
def GetRandom():
    k=random.randint(1,29)
    if(arr[k-1]==0): 
        arr[k-1]=1
        print(k)
    else:
        GetRandom()

def _Random(n):
    i=0
    while(i<n):
        i=i+1
        GetRandom()

_Random(15)
