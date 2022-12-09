from scipy import integrate as integrate
import math

def func(t):
    return math.e**t

t= int(input("enter a number"))
print(integrate.quad(func,1,100,args=t))
