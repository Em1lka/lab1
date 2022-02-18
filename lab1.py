Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a            
        a, b = b, a + b    

for n in fibonacci(100):   
    print(n)               
