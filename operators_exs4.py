#Жители страны Малевии часто экспериментируют с планировкой комнат.
#Комнаты бывают треугольные, прямоугольные и круглые. 
#Чтобы быстро вычислять жилплощадь, требуется написать программу,
#на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
#которая бы выводила площадь получившейся комнаты.
#Для числа π в стране Малевии используют значение 3.14.
#
#Формат ввода, который используют Малевийцы:
#треугольник
#a
#b
#c
#где a, b и c — длины сторон треугольника
#
#прямоугольник
#a
#b
#где a и b — длины сторон прямоугольника
#
#круг
#r
# put your python code here
square = input()

if square == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)


if square == "прямоугольник":
    a = int(input())
    b = int(input())
    S = a * b
    print(S)

if square == "круг":
    r = int(input())
    π = 3.14
    S = π * r**2
    print(S)