import math

def msquare(mul):
    mu = mul * mul
    return mu
call1=msquare(4)
print(call1)

def mult(num1, num2):
    nu = num1 * num2
    assert num1 != 0
    return nu
call2= mult(5, 6)
print(call2)

#Refactored code:

def area_square(length):
    area_sq= length * length
    return area_sq

area_sq1=area_square(5)
print("area of square:"+ str(area_sq1))

def area_triangle(base, height):
    area_tr= 0.5*base*height
    return area_tr
area_tr1=area_triangle(12, 12)
print("area of triangle:"+ str(area_tr1))

