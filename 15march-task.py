'''
#for and while loops
colours=["red","green","yello","white","brown"]
print(len(colours))
max_len=1
for i in colours:
    if len(i)>=max_len:
        max_len= len(i)
        s=i
    #else:
        #print("not in colour")
print("maximum length colour:" +s)


List1 = ["apples","bananas","pineapples"]
Shop_list = [ "apples", "apples", "bananas", "apples", "pear", "pineapples", "pear", "apples","bananas"]
for item in List1:
    s=Shop_list.count(item)
    print("Count of item : " + item + " in Shop_List from List1 is "+ str(s))


#finding the nth even number
lst = []
for n in range(20):
    if n % 2 == 0:
        print(n)
        lst.append(n)

print(lst)
d = lst[2]
print(d)


languages = ['Swift', 'Python', 'Go', 'JavaScript']
# access items of a list using for loop
for language in languages:
    print(language)


# use of range() to define a range of values
values = range(4)
# iterate from i = 0 to i = 3
for i in values:
    print(i)
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")



# program to display numbers from 1 to 5
# initialize the variable
i = 1
n = 5
# while loop from i = 1 to 5
while i <= n:
    print(i)



# program to calculate the sum of numbers
# until the user enters zero
total = 0
number = int(input('Enter a number: '))
# add numbers until number is zero
while number != 0:
    total += number  # total = total + number
    # take integer input again
    number = int(input('Enter a number: '))
print('total =', total)


counter = 0
while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

#brake and contune and pass

for i in range(5):
    if i == 3:
        break
    print(i)


# program to find first 5 multiples of 6
i = 1
while i <= 10:
    print('6 * ', (i), '=', 6 * i)
    if i >= 5:
        break
    i = i + 1


for i in range(5):
    if i == 3:
        continue
    print(i)

# program to print odd numbers from 1 to 10

num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)


n = 10
# use pass inside if statement
if n > 10:
    pass
print('Hello')


#if statment
number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')
print('The if statement is easy')


number = 10
if number > 0:
    print('Positive number')
else:
    print('Negative number')
print('This statement is always executed')



number = 0
if number > 0:
    print("Positive number")
elif number == 0:
    print('Zero')
else:
    print('Negative number')
print('This statement is always executed')



number = 5
# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
        print('Number is 0')
    # inner else statement
    else:
        print('Number is positive')
# outer else statement
else:
    print('Number is negative')
# Output: Number is positive
'''

#range
for i in range(-10,2,3):
    print(i)













