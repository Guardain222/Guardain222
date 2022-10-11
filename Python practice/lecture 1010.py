"""""
a = ["Blue", "red", "green"]
 # to delete a item in the list use
 # del a[The postiion of the item you want to delete]
 # to add a value u can 
 a[Blue] = ["Green"]

print (a)
"""""

"""""
#Dictionaries {} # is used to look up something quickly
#         key    value
en2fr = {"one": "un", "two": "Deux", "Three" : "Trois"}
#to find the class of the thing
print (type (en2fr))
#to print the certain type of value using the key 
print (en2fr ["two"])
d ={1 : "Hello", "CM1101" : True, 3.14: ["red", "Blue","Green"]}
print (d [1])
#one key only to one value, no one key can have 2 values
"""""
"""""
# definitio functions
def add(a,b):
    result = a + b
    return result

#to call a function
# we need to add arguments in the parentisi
print (add(3,4))

def welcome_to_town(town):
    print ("Welcome to", town)

def welcome_by_name(name):
    print ("Hello")

def gretting(town, name):
    welcome_to_town(town)
    welcome_by_name(name)

gretting("Cardiff", "Kirill")
"""""
"""""
def add (a,b):
    return a + b
# can define a function to a variable
f = add 
print (f(2,3))

def sub (a , b):
    return a - b

funcs = [add , sub]
print (funcs[0](3,4))
#retry at home
def do_arithemetic(what,a,b):
    return what (a,b)

print (do_arithemetic(add,3,4))
"""""
"""""
def make_multiplier():
    def mul(a,b):
        return a * b
    return mul

f = make_multiplier
print (f(3,4))
"""""
"""""
def compose (f,g):
    def composition (x):
        return (f(g(x)))
    return composition

def double(x):
    return 2 * x

def square (x):
    return x*x

c = compose(square, double )
print (c(4))
"""""
"""""
#meeds work
from tokenize import Double


def diff(fun):
    dx = 0.0001
    def deriv(x):
        return (fun(x + dx) - fun(x)) / dx
    return deriv 

d_double = diff(Double)
print(d_double (2))
"""""
