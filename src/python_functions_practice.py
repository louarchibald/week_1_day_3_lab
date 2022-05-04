def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    return num1 - num2

def length_of_string(test_string):
    return len(test_string)

def add_string_as_number(string1, string2):
    num1 = int(string1)
    num2 = int(string2)
    return num1 + num2

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(month3):
    return months [month3 -1]

def number_to_short_month_name(month4):
    month = months[month4 -1]
    return month[:3]