
#? 1-The program takes a command line argument, this argument is the name of a text file.
#? the program reads all the text and split them and calulate the 20 most used workds in the
#? file
#? and then write them to a file called popular
#? words.txt

# import sys

# if len(sys.argv) < 2:
#     print('Please enter the name of the input file when running!')
#     sys.exit(1)

# try:
#     file = open(sys.argv[1], 'r')
#     content = file.read().split()
#     file.close()
# except Exception as e:
#     print("Input file not found")

# hashmap = {}
# for word in content:
#     if word in hashmap:
#         hashmap[word] += 1
#     else:
#         hashmap[word] = 1


# sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

# file2 = open('popular_words.txt', 'w')
# count = 0
# for count, (item, freq) in enumerate(sorted_hashmap.items()):
#     file2.write(f"{count+1}. {item}: {freq}\n")
#     count += 1
#     if count == 20:
#         file2.close()
#         break
# file2.close()

#? 2-Given two points represented as x1, y1, x2, y2, r the (float)return (float) distance
#? between
#? them considering the following distance equation.

# from math import sqrt, pow
# def calculate_dist(x1,y1, x2,y2):
#     return sqrt(pow(y2 - y1, 2) + pow(x2 - x1, 2))

# print(calculate_dist(1,1,1,5))

#? 3-Create a Vehicle class without any variables and methods

# class Vehicle:
#     pass

#? 4-Create a Vehicle class with max-speed and mileage instance attributes

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

#? 5-Write a Python program to reverse a string word by word.

# def reverse_words(string):
#     string = string.split()
#     right = len(string) - 1
#     left = 0
#     while left < right:
#         temp = string[left]
#         string[left] = string[right]
#         string[right] = temp
#         left += 1
#         right -= 1
#     return ' '.join(string) 
# string = "Hello world, This is me reversing this string!"
# reversed_string = reverse_words(string)
# print(reversed_string)


#? 6-Write a Python class which has two methods get_String and print _String. get_String
#? accept a string from the user and print_String print the string in upper case

# class String_methods:
#     def get_String(self):
#         str = input("Enter the string: ")
#         self.print_String(str)
#     def print_String(self,str):
#         print(str.upper())

# instance = String_methods()
# instance.get_String()

# 7-Write a Python class named Circle constructed by a radius and two methods which will
# compute the area and the perimeter of a circle.

# from math import pi, pow
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def compute_area(self):
#         print(f"Circle's area: {round(pi * pow(self.radius, 2), 2)}")
#     def compute_circumference(self):
#         print(f"Circle's circumference: {round(pi * self.radius * 2, 2)}")

# circle = Circle(4)
# circle.compute_area()
# circle.compute_circumference()