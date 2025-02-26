from problem01_classes import Cube, Sphere
    
c1 = Cube(12.5, "cm")
s1 = Sphere(12.5, "cm")

c2 = Cube(2.5, "m")
s2 = Sphere(2.5, "m")

diffv = c1 - s1
sumv = s1 + c2

print(f"Difference volume in m3 is {diffv:.2f}")
print(f"Summation volume in m3 is {sumv:.2f}")

print(c2-c1)
print(s1+s2)
print(c2-s2)
print(s2-c1)

