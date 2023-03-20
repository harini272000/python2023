
#function that returns the maximum value from a list of numbers:
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

result = find_max([2, 6, 3, 8])
print(result)


def number():
    nums = [1, 2, 2, 3, 4, 5, 4, 4, 5, 5, 6, 7]
    nums1 = list()
    nums1.append(nums[0])
    for item in nums:
        if item != nums1[-1]:
            nums1.append(item)
            #return nums1
    print(nums1)
number()

#function that prints a message a given number of times:

def print_message(message, times):
    for i in range(times):
        print(message)

print_message("Hello", 3)

# while return is used to exit a function and return a value to the caller.
def sum(a,b):
    e=a+b
    return e
e=sum(2,3)
print(e)
f=e*5
print(f)

#No return value and without Argument
def even_or_odd():
    n=int(input('enter a number: '))
    if n%2==0:
        print('{} is even'.format(n))
    else:
        print('{} is odd'.format(n))
even_or_odd()


#Return value and with Arguments
def even_or_odd(n):
    if n%2==0:
        return ('it is even')
    else:
        return ('it is odd')
result=even_or_odd(90)
print(result)

#Return value and without Argument
def even_or_odd():
    n=int(input('enter a number: '))
    if n%2==0:
        return ('{} is even'.format(n))
    else:
        return ('{} is odd'.format(n))
result=even_or_odd()
print(result)


#No return value and with Arguments
def even_or_odd(n):
    n=int(input('enter a number: '))
    if n%2==0:
        print('{} is even'.format(n))
    else:
        print('{} is odd'.format(n))
even_or_odd(30)

# function that adds two numbers:
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)

#function that calculates the area of a rectangle:

def rectangle_area(width, height):
    return width * height

result = rectangle_area(3, 4)
print(result)

#function that checks if a number is even or odd:

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(5)
print(result)


# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ',sum)

add_numbers(1,2)


def square_value(num):
    return num ** 2

print(square_value(2))
print(square_value(-4))
