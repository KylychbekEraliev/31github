def function1():
    print('hello world')
    print("hello world2")
print('this is outside of function, just to make sure that our function works')


def function2(x):
    return 2*x
a = function2(2)
print(a)
b = function2(5)
print(b)

def function3(x,y,z):
    return x+y+z

d = function3(2,4,5)
print(d)


name = "kylych"
height_cm = 1.79
weight_kg = 74

name1 = "Roza"
height_cm1 = 1
weight_kg1 = 1

def bmi_function(name,height_cm,weight_kg):
    bmi= weight_kg/ (height_cm**2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + "is not overweight"
    else:
        return name + " is overweight"
    

result1=bmi_function(name,height_cm,weight_kg)
print(result1)
result1=bmi_function(name1,height_cm1,weight_kg1)
print(result1)