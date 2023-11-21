#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    
    while i > 0:
        print(i)
        i -= 1
        print("Happy New Year!")
        


def square_integers(int_list):
    # code goes here!

    square_integers = [num ** 2 for num in int_list]
    return square_integers

def fizzbuzz():
    # code goes here!
    
    for num in range(1, 101):
        output = ""
        if num % 3 == 0:
            output += "Fizz"
        if num % 5 == 0:
            output += "Buzz"
        print(output or num)

# Call the function to see the output
fizzbuzz()

