    #Complex Datatype Practice Program
import math
import cmath
a=4+9j
print("The real part of {} is {}".format(a,a.real))
print("The imaaginary part of {} is {}".format(a,a.imag))

#Complex datatype arithmatic operations
a=4+9j
b=7-3j
c=8-1j
sum=a+b+c
mul=a*b*c
sub=a-b-c
div=a/b/c
print("The sum of {}, {} and {} is {}".format(a,b,c,sum))
print("The Multiplication of {}, {} and {} is {}".format(a,b,c,mul))
print("The substraction of {}, {} and {} is {}".format(a,b,c,sub))
print("The division of {}, {} and {} is {}".format(a,b,c,div))

#Magnitude of a=4+9j =Root of (4^2+9^2)
print(abs(a))
#Conjugate of a= 4+9j is 4-9j
print(a.conjugate())

#Getting the phase (angle) of the complex number a=4+9j
print(cmath.phase(a))
#Getting the polar form of a complex number a=4+9j(magnitude and angle)
print(cmath.polar(a))
#Getting the sqrt of the complex number a=4+9j
print(cmath.sqrt(a))
