import math
def reverse_name(name):
    first_name, last_name = name.split(" ")
    print(last_name + " " + first_name)

def n_nn_nnn(n, ith):
    total = 0
    rest = 0
    for i in range(ith):
        highest_digit = (10 ** i) * n
        rest += highest_digit
        total += rest
        print(highest_digit, rest, total)
    print(total)

def print_sample():
    print('''a string that you "don't" have to escape''')
    print(f"This\nis a ........... multi-line")
    print("heredoc string --------> example")

def sphere_volume(radius):
    return 4/3 * math.pi * radius ** 3

def triangle_area(base, height):
    return 0.5 * base * height

def draw_stars(rows):
    for i in range(0, rows + 1):
        print("* " * i)
    for i in range(rows - 1, 0, -1):
        print("* " * i)

def reverse_word(word):
    return word[::-1]

def print_not_divisble_by_3(n):
    for i in range(0,n+1):
        if not (i % 3):
            continue
        else:
            print(i)
def recursive_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)

def fibonacci(num):
    last = 1
    current = 1
    print(last, end=' ')
    for i in range(num - 1):
        print(current, end=' ')
        temp = current
        current += last
        last = temp

def calculate_chars_nums(string):
    nums = 0
    chars = 0
    for i in string:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            chars += 1
        elif (i >= '0' and i <= '9'):
            nums += 1
    return [nums, chars]

'''
1- Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
'''
name = input("Enter first and last name: ")
reverse_name(name) 

'''
2- Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''
n_nn_nnn(5, 3)

'''
3- Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

print_sample()

'''
4- Write a Python program to get the volume of a sphere with radius 6.
'''
sphere_volume1 = round(sphere_volume(6), 2)
print(sphere_volume1)

'''
5- Write a Python program that will accept the base and height of a triangle and compute
the area.
'''
triangle_area1 = round(triangle_area(3,4), 2)
print(triangle_area1)

'''
6- Write a Python program to construct the following pattern, using a nested for loop.
Search about method
end=””
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
draw_stars(5)

'''
7- Write a Python program that accepts a word from the user and reverse it.
'''
word = input("Enter the word: ")
reversed_word = reverse_word(word)
print(reversed_word)

'''
8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
'''
print_not_divisble_by_3(6)

'''
9-Write a Python program to get the Fibonacci series between 0 to 50
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
'''
#method 1 using recursion
n = int(input("enter the number of elements you want to create fibonacci series: "))
for i in range(n + 1):
    if recursive_fibonacci(i) == 0:
        continue
    print(f"{recursive_fibonacci(i)}", end=' ')

#method 2 (normal loop)
n = int(input("enter the number of elements you want to create fibonacci series: "))
fibonacci(n)

'''
10- Write a Python program that accepts a string and calculate the number of digits and letters
'''
nums, chars = calculate_chars_nums(input("Enter the word you want to count: "))
print(f"the word has {nums} numbers and {chars} letters.")