import numpy as np #import numpy library

#integers

i=10 #integer
print(type(i)) #print out the data type of 1

a_i=np.zeros(i,dtype=int) #declare an array of ints
print(type(a_i))          #will return ndarray
print(type(a_i[0]))       #will return int64

#floats

x=119.0          #floating point number
print(type(x))   

y=1.19e2
print(type(y))

z=np.zeros(i,dtype=float)
print(type(z))
print(type(z[0]))