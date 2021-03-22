#Напишите программу, которая получает на вход три целых числа, 
#по одному числу в строке, и выводит на консоль в три строки сначала максимальное, 
#потом минимальное, после чего оставшееся число.
#
#На ввод могут подаваться и повторяющиеся числа.
a = int(input())
b = int(input())
c = int(input())

#d = max(a, b, c)

#e = min(a, b, c)

if a < b and b < c:
    print(c)
    print(a)
    print(b)


if c < b and b < a:
    print(a)
    print(c)
    print(b)

if b < a and a < c:
    print(c)
    print(b)
    print(a)

if a < c and c < b:
    print(b)
    print(a)
    print(c)

if c < a and a < b:
    print(b)
    print(c)
    print(a)

if b < c and c < a:
    print(a)
    print(b)
    print(c)

#23 23 21
if a == b > c:
    print(a)
    print(c)
    print(b)

if c == b > a:
    print(c)
    print(a)
    print(b)

if c == a > b:
    print(c)
    print(b)
    print(a)

if a == b < c:
    print(c)
    print(a)
    print(b)

if c == b < a:
    print(a)
    print(c)
    print(b)

if c == a < b:
    print(b)
    print(c)
    print(a)
    
if c == a == b:
    print(b)
    print(c)
    print(a)