# question 1: write a function to print "hello_USERNAME"
def hello_name(user_name):
    print(f'hello_{user_name}!')
hello_name("USERNAME")

# question 2: write a function that prints odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(1,101):
        if num % 2 == 1:
            print(num)
first_odds

# question 3: write a function to return the max number of a list
def max_num_in_list(a_list):
    max_ = a_list[0]
    for num in a_list:
        if num > max_:
            max_ = num
    return max_
a_list = [1,2,3,4,5,6,7,8,9]
max_list = max_num_in_list(a_list)
print(max_list)

# question 4: write a function to return if a given year is a leap year, return should be a boolean type
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
a_year = 2022
if is_leap_year(a_year):
    print(str(a_year) + " is a leap year!")
else:
    print(str(a_year) + " is not a leap year.")

# question 5: write a function to see if all numbers in a list are consecutive, return should be a boolean type
def is_consecutive(a_list):
    consecutive_list = list(range(min(a_list), max(a_list)+1))
    if a_list == consecutive_list:
        return True
    else:
        return False
a_list = [1,2,3,4,5]
if is_consecutive(a_list):
    print(str(a_list) + " is consecutive.")
else:
    print(str(a_list) + " is not consecutive.")