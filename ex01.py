from problem01_classes import Cube, Cubes, Sphere, Spheres, Shapes
    
cube1 = Cube(2, "m")

text = cube1.info()
print(text)

cube2 = Cube(5, "cm")
print(cube2.info())

print("="*20)

my_cubes = Cubes()
text = my_cubes.cubes_info()
print(text)

my_cubes.add_cube(cube1)
my_cubes.add_cube(cube2)


print(my_cubes.cubes_info())

print("="*20)

sphere1 = Sphere(1, "m")
sphere2 = Sphere(3, "cm")
sphere3 = Sphere(23.5, "cm")

sphere4 = Sphere(99.9, "m")


my_spheres = Spheres()
my_spheres.add_sphere(sphere1)
my_spheres.add_sphere(sphere2)
my_spheres.add_sphere(sphere3)
print(my_spheres.spheres_info())
print(sphere4.info())

print("="*20)

shapes = Shapes(my_cubes, my_spheres)
print(shapes.all_shapes_info())

