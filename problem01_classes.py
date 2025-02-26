# import math
#
#
# class Shapes:
#     def __init__(self, cube_shapes, sphere_shapes):
#         self.__cube_shapes = Cubes
#         self.__sphere_shapes = Shapes
#
#     def Shapes(self, cube_shapes, sphere_shapes):
#         pass
#
#     def all_shapes_info(self):
#         return (f'Total volume in cubic meters: {Shapes.total_volume_m(Shapes)} m3\n'
#                 f'Total volume in cubic centimeters: {Shapes.total_volume_cm(Shapes)} cm3')
#
#     def total_volume_m(self):
#         pass
#
#     def total_volume_cm(self):
#         pass
#
#
# class Cubes:
#     def __init__(self):
#         self.__cubes = []
#
#     @property
#     def list_cubes(self):
#         return self.__cubes
#
#     @list_cubes.setter
#     def list_cubes(self, cubes):
#         self.__cubes = cubes
#
#     def Cubes(self):
#         Cube.info(Cube)
#
#     def get_cubes(self):
#         pass
#         # self.__cubes.append(Cube.info(Cube))
#
#     def add_cube(self, cube):
#         self.__cubes.append(Cube)
#
#     def cubes_info(self):
#         print('Cubes: ')
#
#         if self.__cubes == []:
#             print("No cubes available")
#         else:
#             for i in range(len(self.__cubes)):
#                 print(f'{i + 1}. {self.__cubes[i]}')
#
#
# class Cube(Cubes):
#     def __init__(self, side: float, unit: str, volume: float = 0):
#         super().__init__()
#         self.__side = side
#         self.__unit = unit
#         self.__volume = volume
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, side):
#         self.__side = side
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, volume):
#         self.__volume = volume
#
#     def Cube(self, side: float, unit: str):
#         if side < -1:
#             raise ValueError("The values are invalid")
#
#         if not isinstance(unit, str):
#             raise TypeError("Type error")
#
#         self.__cubes.append(Cube.info())
#
#     def info(self):
#         self.__volume = self.__side ** 3
#         if self.__unit == 'm':
#             unit = 'm3'
#         elif self.__unit == 'cm':
#             unit = 'cm3'
#         # result = f'Cube with side {self.__side:.2f}{self.__unit}, volume: {self.__volume:.2f}{unit}'
#         # self.__cubes.append(result)
#         # return result
#         print(f'Cube with side {self.__side:.2f}{self.__unit}, volume: {self.__volume:.2f}{unit}')
#
#
# class Spheres:
#     def __init__(self):
#         self.__spheres = []
#
#     @property
#     def list_spheres(self):
#         return self.__spheres
#
#     @list_spheres.setter
#     def list_sphere(self, sphere):
#         self.__spheres = sphere
#
#     def Spheres(self):
#         pass
#         # self.__cubes.append()
#
#     def get_spheres(self):
#         self.__spheres.append(Sphere.info(Sphere))
#
#     def add_sphere(self, sphere):
#         sphere = Sphere
#
#     def spheres_info(self):
#         print('Spheres:')
#         if self.__spheres == []:
#             print("No Sphere available")
#         else:
#             for i in range(len(self.__spheres)):
#                 # i += 1
#                 print(f'{i + 1}. {self.__spheres[i]}')
#
#
# class Sphere(Spheres):
#     def __init__(self, radius: float, unit: str):
#         super().__init__()
#         if radius < -1:
#             raise ValueError("The values are invalid")
#
#         if not isinstance(unit, str):
#             raise TypeError("Type error")
#         #
#         # if not unit == 'm' or 'cm':
#         #     raise ValueError("The values are invalid")
#         self.__radius = radius
#         self.__unit = unit
#         self.__volume = 0
#
#     def Sphere(self, radius: float, unit: str):
#         if radius < -1:
#             raise ValueError("The values are invalid")
#
#         if not isinstance(unit, str):
#             raise TypeError("Type error")
#         self.__spheres.append(Sphere.info())
#
#
#     def info(self):
#         self.__volume = math.pi * (self.__radius**2)
#         if self.__unit == 'm':
#             unit = 'm3'
#         elif self.__unit == 'cm':
#             unit = 'cm3'
#         return (f'Sphere with radius {self.__radius:.2f}{self.__unit},'
#                 f' volume: {self.__volume:.2f}{unit}')
#
#
# class MagicOperation:
#     def __add__(self, other):
#         pass
#
#     def __sub__(self, other):
#         pass
#
#     def volume_in_m(self):
#         pass

import math


class Shapes:
    def __init__(self, cube_shapes, sphere_shapes):
        self.__cube_shapes = cube_shapes
        self.__sphere_shapes = sphere_shapes

    def all_shapes_info(self):
        cubes_info = self.__cube_shapes.cubes_info()
        spheres_info = self.__sphere_shapes.spheres_info()

        return (f"All Shapes Information:\n"
                f"{cubes_info}\n"
                f"{spheres_info}\n"
                f"{self.total_volume_m()}\n"
                f"{self.total_volume_cm()}\n")

    def total_volume_m(self):
        total = 0.00
        for cubes in self.__cube_shapes.get_cubes():
            if cubes.unit == "m":
                total += cubes.volume
            elif cubes.unit == "cm":
                total += cubes.volume * 0.000001
        for spheres in self.__sphere_shapes.get_spheres():
            if spheres.unit == "m":
                total += spheres.volume
            elif spheres.unit == "cm":
                total += spheres.volume * 0.000001
        return f"Total volume in cubic meters: {total:.2f}m³"

    def total_volume_cm(self):
        total = 0.00
        for cubes in self.__cube_shapes.get_cubes():
            if cubes.unit == "cm":
                total += cubes.volume
            elif cubes.unit == "m":
                total += cubes.volume * 1000000
        for spheres in self.__sphere_shapes.get_spheres():
            if spheres.unit == "cm":
                total += spheres.volume
            elif spheres.unit == "m":
                total += spheres.volume * 1000000
        return f"Total volume in cubic centimeters: {total:.2f}cm³"


class Cubes:
    def __init__(self):
        self.__cubes = []

    @property
    def cubes(self):
        return self.__cubes

    def get_cubes(self) -> list:
        return self.__cubes

    def add_cube(self, cube):
        self.__cubes.append(cube)

    def cubes_info(self) -> str:
        if not self.__cubes:
            return (f"Cubes:\n"
                    f"No cubes available")

        info = "Cubes:\n"
        for i, cube in enumerate(self.__cubes):
            info += f"{i + 1}. Cube with side {cube.side:.2f}{cube.unit}, volume: {cube.volume:.2f}{cube.unit}³\n"
        return info.strip()


class Spheres:
    def __init__(self):
        self.__spheres = []

    def get_spheres(self) -> list:
        return self.__spheres

    def add_sphere(self, sphere):
        self.__spheres.append(sphere)

    def spheres_info(self) -> str:
        if not self.__spheres:
            return (f"Spheres:\n"
                    f"No spheres available")

        info = "Spheres:\n"
        for i, sphere in enumerate(self.__spheres):
            info += (f"{i+1}. Sphere with radius {sphere.radius:.2f}{sphere.unit}, "
                     f"volume {sphere.volume:.2f}{sphere.unit}³\n")
        return info.strip()


class MagicOperation:

    @property
    def volume(self):
        return self.volume

    @property
    def unit(self):
        return self.unit

    def __add__(self, other) -> float:
        if not isinstance(other, (Cube, Sphere)):
            raise ValueError("Type does not match")
        return self.volume_in_m() + other.volume_in_m()

    def __sub__(self, other) -> float:
        if not isinstance(other, (Cube, Sphere)):
            raise ValueError("Type does not match")
        return self.volume_in_m() - other.volume_in_m()

    def volume_in_m(self) -> float:
        if self.unit == "m":
            return self.volume
        elif self.unit == "cm":
            return self.volume * 0.000001


class Cube(MagicOperation):
    def __init__(self, side: float, unit: float):

        if not isinstance(side, (int, float)):
            raise TypeError("Type does not match")
        if side < 0:
            raise ValueError("The values are invalid")

        if not isinstance(unit, str):
            raise TypeError("Type does not match")
        if unit not in {"cm", "m"}:
            raise ValueError("The value are invalid")

        self.__side = side
        self.__unit = unit
        self.__volume = self.__side ** 3

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        if not isinstance(side, (int, float)):
            raise TypeError("Type does not match")
        if side < 0:
            raise ValueError("The values are invalid")
        self.__side = side

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        if not isinstance(unit, str):
            raise TypeError("Type does not match")
        if unit not in {"cm", "m"}:
            raise ValueError("The value are invalid")
        self.__unit = unit

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if not isinstance(volume, (int, float)):
            raise TypeError("Type does not match")
        if volume < 0:
            raise ValueError("The value are invalid")

    def info(self):
        return f"Cube with size {self.__side:.2f}{self.__unit}, volume: {self.__volume}{self.__unit}³"


class Sphere(MagicOperation):
    def __init__(self, radius: float, unit: str):
        if not isinstance(radius, (int, float)):
            raise TypeError("Type does not match")
        if radius < 0:
            raise ValueError("The values are invalid")

        if not isinstance(unit, str):
            raise TypeError("Type does not match")
        if unit not in {"cm", "m"}:
            raise ValueError("The value are invalid")

        self.__radius = radius
        self.__unit = unit
        self.__volume = (4/3) * math.pi * (self.__radius ** 3)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Type does not match")
        if radius < 0:
            raise ValueError("The values are invalid")
        self.__radius = radius

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        if not isinstance(unit, str):
            raise TypeError("Type does not match")
        if unit not in {"cm", "m"}:
            raise ValueError("The value are invalid")
        self.__unit = unit

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if not isinstance(volume, (int, float)):
            raise TypeError("Type does not match")
        if volume < 0:
            raise ValueError("The value are invalid")

    def info(self):
        return f"Sphere with size {self.__radius:.2f}{self.__unit}, volume: {self.__volume:.2f}{self.__unit}³"
