from problem01_classes import Cube, Sphere

try:    
    c1 = Cube(12.5, "xx")
except Exception as e:
    print(type(e))
    print(e)

try:    
    s1 = Sphere(-5, "cm")
except Exception as e:
    print(type(e))
    print(e)
    

s1 = Sphere(0, "m")
c1 = Cube(1000, "cm")

try:    
    x = s1 + 5
except Exception as e:
    print(type(e))
    print(e)

try:    
    x = s1 + c1
    print(x)
except Exception as e:
    print(type(e))
    print(e)


