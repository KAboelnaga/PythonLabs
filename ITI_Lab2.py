import random
# 1- Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list

#method 1: modifying in the same list
def unique_list1(arr):
    return list(set(arr))

# #method 2: creating a new unique list
def unique_list2(arr):
    newlist = []
    for i in arr:
        if i not in newlist:
            newlist.append(i)
    return newlist 

print(unique_list1([1,2,3,3,4,5,5,5]))
print(unique_list2([1,1,2,3,2,4,5,5,5]))

# 2- Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)

def combine_strings(a, b):
    a_front = a[ : (len(a) + 1) // 2]
    b_front = b[ : (len(b) + 1) // 2]
    a_back = a[(len(a) + 1) // 2 : ]
    b_back = b[(len(b) + 1) // 2 : ]
    return (a_front + b_front) + (a_back + b_back)

print(combine_strings('abcde', 'efgh'))

# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False

#? method 1: simply create a new unique list and check length

def unique_list(li):
    if len(list(set(li))) == len(li):
        return True
    return False

#? method 2: check for the number of occurences for each item in the list

def unique_list3(li):
    for i in li:
        if li.count(i) > 1:
            return False
    return True

print(unique_list([1,2,3,4,5]))
print(unique_list([1,1,2,2,3,4,5]))
print(unique_list3([1,2,3,4,5])) 
print(unique_list3([1,1,2,2,3,4,5]))

# 4- Given unordered list, sort it using algorithm bubble sort
# ( read about bubble sort and try to implement it)

def bubble_sort(li):
    for i in range(len(li)):
        flag = True
        for j in range(len(li) - 1):
            k = j + 1
            if li[j] > li[k]:
                temp = li[j]
                li[j] = li[k]
                li[k] = temp
                flag = False
        if flag:
            break
    return li

print(bubble_sort([5,4,3,2,1]))

# 5- Gusses game
# ● Your game generates a random number and gives only 10 tries for the user to
# guess that number.
# ● Get a user input and compare it with the random number
# ● Display a hit message to the user in case the use number is smaller or bigger of
# the random number
# ● If the user type number is out of range(100), display a message that is not allowed
# and don’t count this as try.
# ● If user type a number that has been entered before, display a hint message and
# don’t count this as try
# ● In case the user entered a correct number within the 10 tries, display a
# congratulations message and let your application guess another random number
# with the remain number of tries
# ● If the user finishes all his tries, display a message to ask him if he wants to play
# again or not.

def repeat_guess_game(repeat):
    if repeat == 'Y' or repeat == 'y':
        guess_game()
    elif repeat == 'n' or repeat == 'N':
        return
    else:
        inp = input('invalid input! please enter Y or N!')
        repeat_guess_game(inp)

def guess_game():
    target = random.randint(0, 100)
    tries = 10
    prev_guesses = []
    while tries > 0:
        guess = int(input('enter your guess: '))
        if guess > 100:
            print('Your guess is out of range!')
            continue
        elif guess in prev_guesses:
            print('You guessed this number before!')
        else:
            prev_guesses.append(guess)
            tries -= 1
            if guess > target:
                print('The target number is lower than you guessed!')
            elif guess < target:
                print('The target number is higher than you guessed!')
            else:
                print('congrats! you guessed the number correctly')
                target = random.randint(0, 100)
                print( 'you have', tries, 'tries left guess with it the new number')
                prev_guesses = []
    repeat = input('you are out of tries, play again? (Y/N): ')
    repeat_guess_game(repeat)

guess_game()

# 6- Make account on Hacker-rank for problem solving
# (bonus)
# And try to solve this problem and send me your submission

#? I submitted this solution on hacker rank and it is correct
 
def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        d1 += arr[i][i]
    for i in range(len(arr)):
        d2 += arr[i][len(arr)-1-i]
    return abs(d1-d2)
