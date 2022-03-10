from datetime import datetime


def problem2():
    # add two numbers
    a = 3
    b = 4
    sum1 = a + b
    print(sum)
    # oR
    c = int(input("please enter a num:,"))
    d = int(input("please enter a num:,"))
    sum1 = c + d
    print(sum)


#
def problem3():
    # get quotion of division of two number
    c = int(input("please enter a num:,"))
    d = int(input("please enter a num:,"))
    division = c / d
    print(division)


#
def problem4():
    c = int(input("please enter first num:,"))
    d = int(input("please enter second num:,"))
    e = int(input("please enter third num:,"))
    f = int(input("please enter forth num:,"))
    sum4 = c + d + e + f
    print("sum of four numbers :", sum4)


#
def problem5():
    # 04 Sum and average of marks of five students taken from the user
    student1 = int(input("Please Enter the marks of fist student"))
    student2 = int(input("Please Enter the marks of second student"))
    student3 = int(input("Please Enter the marks of third student"))
    student4 = int(input("Please Enter the marks of forth student"))
    student5 = int(input("Please Enter the marks of fifth student"))
    sum = student1 + student2 + student3 + student4 + student5
    total_no = 5
    average = sum / total_no
    print("sum of five students and their average:", sum, average)


#
def problem6():
    # 05 Percentage of total marks of four students.
    student1 = 40
    student2 = 499
    student3 = 300
    student4 = 302

    sum = student1 + student2 + student3 + student4
    total_no_of_students = 4
    average = sum / total_no_of_students
    Total_marks = 550
    Percentage = sum / 550 * 100
    print("sum of four students:", sum)
    print("the average of four students:", average)
    print("percentage of total marks of four student:", Percentage)


def problem7():
    # 06  Check if a number is greater than 80, say “good”, if not say, “Try again”
    number = int(input("please enter a number:"))
    if number >= 80:
        print("good")
    else:
        print("Try again")


#. Check whether a number is divisible by another user-given number or not.
# TODO
def problem8():
    number = 10
    user_num = int(input("please enter a number: "))
    if number % user_num == 0:
        print("given number is divisible by user number")
    else:
        print("given number is not  divisible by user number")


# sum of odd numbers from 10 user-given numbers
def problem9():
    sum = 0
    count = 1
    while True:
        user_num = int(input("please enter numbers: "))
        if user_num %2 != 0:
            sum = sum + user_num
            count = count + 1
            if count == 10:
                break
        else:
            print("Please enter an odd number ")
    print(sum)

# TODO
# . Sum of even number from n user-given numbers. Where n is also user-input
def problem10():
    sum = 0
    count = 1
    n = int(input("enter n numbers"))
    while True:
        user_num = int(input("please enter numbers: "))
        if user_num % 2 == 0:
            sum = sum + user_num
            count = count + 1
            if count == n:
                break
        else:
            print("Please enter an even number ")
    print(sum)

# Show first n terms of Fibonacci series
def problem11():
    # Program to display the Fibonacci sequence up to n-th term

    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


#
def problem12():
    # Converting temperature from Fahrenheit to Celsius [Formula: C = (f-32) * (5/9)]
    temperature = float(input("enter temperature in fahrenheit: "))
    Celsius = (temperature - 32) * 5 / 9
    print(f"{temperature} in fahrenheit is equal to {Celsius} in Celsius")


# . Calculating pay for an employee, given the hours worked and rate per hour
def problem13():
    hours = int(input("enter hours:"))
    # Calculating pay for an employee, given the hours worked and rate per hour
    hours = float(input("enter hours"))
    r = float(input("enter the rate:"))
    if hours <= 40:
        print(hours * r)
    elif hours > 40:
        print(40 * r + (hours - 40) * 1.5 * r)


# . Determine the status of a student (pass or fail) given his/her marks in a
# subject(passing marks = 50)
def problem14():
    pmarks = float(input("please enter marks :"))
    if pmarks >= 50:
        print("she/ he is pass")
    else:
        print("otherwise she/he is fail")


#
# #. Calculate pay of an employee based on the hours worked. The input includes
# the employee total hours worked this week and their hourly pay rate. The
# employee is to be paid their basic wage for the first 40 hours and time-and-a-half
# (i.e. 50% more) for all hours above 40 (overtime pay). Output the regular pay.
# Overtime pay and total pay for the week on the screen. If the employee worked
# 40 hours or less,don’t output any information about overtime pay.
def problem15():
    total_hours = float(input("please enter  total hours: "))
    hrate_of_pay = float(input("please enter hourly pay rate:"))
    regular_hours = total_hours / 8
    over_time = float(input("please enter over time hours: "))
    if over_time < 40:
        print("does not show any information about overtime")
    elif over_time > 40:
        print("also calculate over time pay")
    else:
        print("nothing to show")

    regular_pay = regular_hours * hrate_of_pay
    over_time_pay = hrate_of_pay * over_time
    total_pay = regular_pay + over_time_pay
    print(regular_pay)
    print(over_time_pay)
    print(total_pay)


# . Take two number from the user and determine the largest number
def problem16():
    num1 = int(input("please enter first num:"))
    num2 = int(input("please enter second num:"))
    if num1 > num2:
        print("num1 is greater than num2")
    else:
        print("num2 is greater than num1")


# . Take three number from the user and determine the largest number.
def problem17():
    num1 = int(input("please enter first num:"))
    num2 = int(input("please enter second num:"))
    num3 = int(input("please enter third num:"))
    if num1 > num2 and num1 > num3:
        print("num1 is the largest number")
    elif num2 > num3 and num2 > num1:
        print("num2 is the largest number ")
    else:
        print("num3 is the largest number ")


# 8. Take four numbers from the user and determine the largest using the most
# suitableapproach from a, b and c given above.
def problem18():
    num1 = int(input("please enter first num:"))
    num2 = int(input("please enter second num:"))
    num3 = int(input("please enter third num:"))
    num4 = int(input(" please enter forth num:"))
    if num1 > num2 and num1 > num3 and num1 > num4:
        print("num1 is te largest number")
    elif num2 > num3 and num2 > num1 and num2 > num4:
        print("num2 is the largest number")
    elif num3 > num4 and num3 > num1 and num3 > num2:
        print("num3 is the largest number")
    else:
        print("num4 is the largest")


# . Determine the grade of a student from the marks obtained (90-100, A; 80-29,
# B;70-79, C; 60-69, D; <60, F)
def problem19():
    marks = int(float("please enter the marks of a student: "))
    if 90 <= marks <= 100:
        print("the grade is: A")
    elif 80 <= marks <= 29:
        print("the grade is: B")
    elif 70 <= marks <= 79:
        print("the grade is: C")
    elif 60 <= marks <= 69:
        print("the grade is: D")
    elif marks < 60:
        print("the grade is: F")
    else:
        print("nothing to show")


# . Input a number and determine whether the number is even or odd.
def problem20():
    num = int(input("please enter a number:"))
    if num % 2 == 0:
        print("the given number is even")
    else:
        print("the given number is odd")


# . Calculate the difference between two times given in 24-hour (hh: mm) format.
def problem21():
    # input time and take difference

    s1 = '10:33'
    s2 = '11:15'  # for example
    FMT = '%H:%M'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    print("difference of two time: ", tdelta)


# input 3 numbers. Determine whether: all are same, all are different or exactly
# twoare same.
def problem22():
    num1 = int(input("please enter first num:"))
    num2 = int(input("please enter second num:"))
    num3 = int(input("please enter third num:"))
    if num1 == num2 and num1 == num3:
        print("all are same number")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print(" exactly two are same")
    else:
        print("all are different number")


# . Finding the sum of 10 numbers taken from the user
def problem23():
    sum = 0
    n = int(input("enter n numbers : "))
    for number in range(1, n+1):
        values = int(input("please enter number:"))
        sum = sum + values
    print("sum of n numbers:", sum)


# . Finding the sum of n numbers taken from the user. Where n is taken from the
# useras well.

def problem24():
    n_numbers = int(input("how many numbers should be sum up?"))
    sum_n = 0
    lstn = []

    for number in range(1, n_numbers + 1):
        n = int(input())
        lstn.append(n)
    print(lstn)
    for ele in range(0, len(lstn)):
        sum_n = sum_n + lstn[ele]
    print("sum of n numbers:", sum_n)


# TODO di it using problem 23 logic
# . Finding the average of n number from the user, where n is user-given value.
def problem25():
    sum = 0
    average_n = 0
    n = int(input("enter n numbers : "))
    for number in range(1, n + 1):
        values = int(input("please enter number:"))
        sum = sum + values
        average_n = sum/n

    print("sum of n numbers:", sum)
    print("average of n numbers:", average_n)




# . Displaying positive integers in the range from 1 to n, where n is taken from the
# user.
# TODO do it using whie True
def problem26():
     n = int(input("please enter n numbers: "))
     # count = 0
     # positive_num = 0
     # while True:
     #     num = int(input("enter values:")
     #     if num > 0:
     #         positive_num += 1
     #         break


     print("positive numbers from n numbers: ", positive_num)


# . Calculate the factorial of a positive integer entered by the user.
def problem27():
    num = int(input("Enter a number: "))
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


# . Take two positive integers a and n from the user. Calculate and display an.
# Assumethat the power operator is not available.
def problem28():
    a = int(input("please enter positive number "))
    n = int(input("please enter positive number"))
    result = a ** n
    # pow()
    print(result)


# . Take three number from the user and determine the largest number. Do it
# using a loop
def problem29():
    list1 = []

    for num in range(0, 3):
        n = int(input("enter numbers: "))
        list1.append(n)

    list1.sort()

    print("Largest element is:", list1[-1])


# Take n number from the user and determine the largest number entered by the
# user,where n is taken from the user as well.
def problem30():
    n = int(input("enter numbers: "))
    A = []
    for num in range(1, n + 1):
        A.append(num)
    print(A)
    max = A[0]
    for x in A:
        if x > max:
            max = x
    print("Largest element is:", max)


# Take n numbers from the user and determine both the smallest and the
# largestnumber entered by the user, where n is taken from the user as well.
def problem31():
    smallest = 0
    largest = 0
    lst1 = []
    n = int(input("please enter numbers:"))
    for i in range(1, n+ 1):
        number = int(input("enter values"))
        lst1.append(number)
        print(lst1)
    for ele in range(n):
        if lst1[ele] >= 0:
            largest = largest + 1
        else:
            smallest = smallest + 1
    print("total numbers of smallest", smallest)
    print("the total numbers of largest:", largest)



# Take n numbers from the user and determine that how many positive and
# negativeintegers were entered by the user.
def problem32():
    lst1 = []
    n_numbers = int(input("please enter numbers: "))
    n_positive = 0
    n_negtive = 0
    for i in range(1, n_numbers + 1):
        number = int(input("enter values"))
        lst1.append(number)
        print(lst1)
    for ele in range(n_numbers):
        if lst1[ele] >= 0:
            n_positive = n_positive + 1
        else:
            n_negtive = n_negtive + 1
    print("total numbers of positive", n_positive)
    print("the total numbers of negtive:", n_negtive)


# Take a positive integer n from the user. Display all the divisors of n.
def problem33():
    n = int(input("Enter an integer:"))
    print("The divisors of the number are:")
    for i in range(1, n + 1):
        if (n % i == 0):
            print(i)


# #nput a positive integer from the user and determine where the number is a perfect
# number or not. (a perfect number is a positive integer that is equal to the sum of
# its proper positive divisors, that is, the sum of its positive divisors excluding the
# numberitself.)
def problem34():
    n = int(input("Enter any number: "))
    sum1 = 0
    for i in range(1, n):
        if n % i == 0:
            sum1 = sum1 + i
    if sum1 == n:
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")


# nput a positive integer from the user and determine whether is a prime number or not.
def problem35():
    # Program to check if a number is prime or not
    num = int(input("Enter a number: "))
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")


# Take a positive integer from the user. Displaying an error message and
# prompting for input again and again if the user enters invalid input (negative or
# zero)
def problem36():
    while True:
        number = input("Enter a number: ")
        try:
            val = int(number)
            if val < 0:  # if not a positive int print message and ask for input again
                print("Sorry, input must be a positive integer, try again")
                continue
            break
        except ValueError:
            print("That's not an int!")
            # else all is good, val is >=  0 and an integer
    print(val)


# algorithm of sum
# def problem37():
# Display negative of a number
def problem38():
    number = int(input("please enter number:"))
    number = number * -1
    print(number)


# . Find absolute of an input. Assume that the absolute operator is not available.
def problem39():
    number = int(input("please enter a number:"))
    if number >= 0:
        print("absolute or positive value:", {number})
    else:
        print("number is not positive")


# Input 2 number and find if both are even, both are odd, or 1 even 1 odd.
def problem40():
    num1 = int(input("please enter first num: "))
    num2 = int(input("please enter second num: "))
    if num1 % 2 == 0 and num2 % 2 == 0:
        print("both are even numbers")
    elif num1 % 2 == 0 or num2 % 2 != 0:
        print("one odd or other even")
    elif num1 % 2 != 0 or num2 % 2 == 0:
        print("one odd or other even")
    else:
        print("both are odd numbers")


# Input 3 numbers and find how many are odd.
def problem41():
    num1 = int(input("please enter first num: "))
    num2 = int(input("please enter second num: "))
    num3 = int(input("please enter third num: "))
    if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0:
        print("three numbers are odd", {num1}, {num2}, {num3})
    elif num1 % 2 == 0 and num2 % 2 != 0 and num3 % 2 != 0:
        print("two number are odd:", {num1}, {num2}, {num3})
    elif num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 != 0:
        print("only one number is  odd:", {num1}, {num2}, {num3})
    elif num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 == 0:
        print("only one number is  even:", {num1}, {num2}, {num3})
    else:
        print("three numbers are even", {num1}, {num2}, {num3})


# TODO
# . Input 3 numbers and print the 2 largest numbers/
# and also find 2nd largest number
def problem42():
    num1 = int(input("please enter first number:"))
    num2 = int(input("please enter second number:"))
    num3 = int(input("please enter third number:"))
    if num1 > num2 and num1 < num3 or num1 < num2 and num1 > num3:
        print("the second largest number is num3:", num1)
    elif num2 > num3 and num2 < num1 or num2 < num3 and num2 > num1:
        print( "the second largest number is num2:", num2)
    else:
        print("the second largest number is num3:", num3)
    if num1 > num2 and num1 > num3:
        print("num1 is the largest number:", num1)
    elif num2 > num3 and num2 > num1:
        print("num2 is the largest number:", num2)
    else:
        print("num3 is the largest number:", num3)

# TODO
# . Input a number and find if it is 2-digit positive integer or not
def problem43():
    while True:
        number = input("Enter a number: ")
        try:
            val = int(number)
            data = str(val)
            if len(data) != 2:
                print("Sorry, input must be 2-digits  positive integer, try again")
                continue
            break
        except ValueError:
            print("That's not an 2-digits integer!")

    print(data)




# . Input a 2-digit number and find the absolute difference between its digits
def problem44():
    while True:
        a = int(input("enter a value:"))
        b = int(input("enter a value:"))
        try:
            val1 = int(a)
            val2 = int(b)
            data1 = str(val1)
            data2 = str(val2)
            if len(data1) != 2:
                print(data1, "  Sorry, input must be 2-digits  positive integer, try again")
                if len(data2) != 2:
                    print(data2, " Sorry, input must be 2-digits  positive integer, try again")
                continue
            if len(data2) != 2:
                print(data2, " Sorry, input must be 2-digits  positive integer, try again")
                continue
            break
        except ValueError:
            print(" both numbers  are not  2-digits integer!")

    print("the absolute difference two number(2-digits number):", abs(val1 - val2))


# nput an integer (up to 4 digits) and store its reverse in another variable.
# Then display both integers.
def problem45():
    number = int(input("enter a number"))
    reverse = 0
    while number > 0:
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10
    print("reverse of given number:", reverse)


# interchange two numbers
def problem46():
    num1 = 9
    num2 = 6
    temp = num1
    num1 = num2
    print(temp)
    print(num2)


# interchange two numbers without using exra variables
def problem47():
    num1 = int(input("please enter first num: "))
    num2 = int(input("please enter second num: "))
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print("the values of num1 after interchang: ", num1)
    print("the values of num2 after interchang: ", num2)


# TODO
# . Conversion of microseconds to weeks, days, hours, minutes, seconds,
# andremaining microseconds.
def problem48():
    import time
    def current_milli_time():
        return round(time.time() * 1000)

    milliseconds = int(round(time.time() * 1000))
    print(milliseconds)
    microseconds = milliseconds * 1, 000
    print(microseconds)
    Micro = microseconds[0]
    weeks = Micro / 604, 800, 000, 000
    days = Micro / 86, 400, 000, 000
    hours = Micro / 3, 600, 000, 000
    minutes = Micro / 60, 000, 000
    seconds = Micro / 1, 000, 000
    print(weeks)
    print(days)
    print(hours)
    print(minutes)
    print(seconds)

    current_milli_time()


## multiply the numbers with the sum of its digits
def problem49():
    num = int(input("enter number: "))
    sum = 0
    multi = 1
    while num > 0:
        digit = num % 10
        sum = sum + digit
        # multi = multi*digit
        num = num // 10
        print(sum)
        # print(multi)


def problem50():
    num1 = int(input("enter first value"))
    num2 = int(input("enter second value"))
    try:
        if num1 % num2 == 0:
            print("YES")
        else:
            print("Not divisible")
    except Exception as e:
        print(e)


# input 2 numbers from the user and print YES if 1st is divisible by 2nd
def problem51():
    num1 = int(input("enter first value"))
    num2 = int(input("enter second value"))
    if num2 % num1 == 0:
        print("YES")
    else:
        print("Not divisible")


# input two numbers and print yes if one number is divisible by the other
def problem52():
    num1 = int(input("enter first value"))
    num2 = int(input("enter second value"))
    if num1 % num2 == 0 and num2 % num1 == 0:
        print("YES")
    elif num1 % num2 == 0 or num2 % num1 == 0:
        print("yes")
    else:
        print("nothing")


# Input numbers till user inputs a zero and display their sum
def problem53():
    sum = 0
    count = 0
    while True:
        number = int(input("please enter number"))
        if number <= 0:
            break
        try:
            sum += float(number)
            count += 1
        except ValueError:
            print("Bad number.  Try again")
    print("You entered %s numbers whose sum is %s." % (count, sum))


# TODO
# Input numbers till user inputs a zero and at the end display last non-zero number
def problem54():
    num = None
    while True:
        number = int(input("please enter a number: "))
        if number == 0:
            if num is None:
                print("No previous non zero Number")
            else:
                print(num)
            break
        else:
            num = number


# Input numbers till user inputs a zero and display the largest number
def problem55():
    largest = 0
    while True:
        number = int(input("please enter number"))
        if number <= 0:
            break
        try:
            fnum = float(number)
        except ValueError:
            print("Invalid input")
            continue

        if largest == 0 or number >= largest:
            largest = number
        else:
            largest = largest

    print("Maximum is", largest)


# Input numbers till user inputs a zero, and display the smallest number
def problem56():
    smallest = 0
    while True:
        number = int(input("please enter number"))
        if number <= 0:
            break
        try:
            fnum = float(number)
        except ValueError:
            print("Invalid input")
            continue
        if smallest == 0 or number <= smallest:
            smallest = number
        else:
            smallest = smallest
    print("Minimum is", smallest)


#input 10 numbers, and display the smallest number
def problem57():
    smallest = 0
    while True:
        number = int(input("please enter number"))
        if number <= 10:
            break
        try:
            fnum = float(number)
        except ValueError:
            print("Invalid input")
            continue
        if smallest == 0 or number <= smallest:
            smallest = number
        else:
            smallest = smallest
    print("Minimum is", smallest)




# Input 10 numbers, and display count of even and odd numbers, separately, at the end
# Input SLimit and Elimit from the user, and display even numbers between
# range,with both limit, included.
# a. Give an efficient solution that does not check divisibility of each number
# in the given range
def problem58():
    lst1 = []
    n_numbers = int(input("please enter numbers: "))
    even_num = 0
    odd_num = 0
    for i in range(1, n_numbers + 1):
        number = int(input("enter values"))
        lst1.append(number)
        print(lst1)
    for ele in range(n_numbers):
        if lst1[ele] % 2 == 0:
            even_num = even_num + 1
        else:
            odd_num = odd_num + 1
    print("total numbers of even", even_num)
    print("the total numbers of odd:", odd_num)

#nput 10 numbers, and display count of even and odd numbers, separately, at the end
def problem58n():
    lst1 = []

    even_num = 0
    odd_num = 0
    for num in range(0, 10):
        num = int(input())
        if num % 2 == 0:
            even_num = even_num + 1
        else:
            odd_num += 1

    print("total numbers of even", even_num)
    print("the total numbers of odd:", odd_num)


# . Input SLimit and ELimit from the user and display only those numbers
# betweenrange which are divisible by 2 or 3 or 5, with both limits included
def problem59_and_60():
    start_limit = int(input("please enter start limit:"))
    end_limit = int(input("please enter the end limit:"))
    for num in range(start_limit, end_limit):
        if num % 3 == 0 and num % 5 == 0 and num % 2 == 0:
            print(str(num) + " ",
                  end="")  # The end parameter is used to append any string at the end of the output of the print statement in python.



# input two numbers and find their GCD
def problem61():
    def GCD_Loop(a, b):
        if a > b:  # define the if condition
            temp = b
        else:
            temp = a
        for i in range(1, temp + 1):
            if (a % i == 0) and (b % i == 0):
                gcd = i
        return gcd

    x = int(input(" Enter the first number: "))  # take first no.
    y = int(input(" Enter the second number: "))  # take second no.
    num = GCD_Loop(x, y)  # call the gcd_fun() to find the result
    print("GCD of two number is: ")
    print(num)  # call num


# . Input 3 numbers and find their GCD
def problem62():
    def GCD_Loop(a, b, c):
        if a > b:  # define the if condition
            temp = b
        elif a > c:
            temp = c
        else:
            temp = a
        for i in range(1, temp + 1):
            if (a % i == 0) and (b % i == 0) and (c % i == 0):
                gcd = i
        return gcd

    x = int(input(" Enter the first number: "))  # take first no.
    y = int(input(" Enter the second number: "))  # take second no.
    z = int(input(" Enter the second number: "))  # take third no.
    num = GCD_Loop(x, y, z)  # call the gcd_fun() to find the result
    print("GCD of three number is: ")
    print(num)  # call num


# TODO
# Input 2 numbers and display their LCM
def problem63():
    def lcm_of_num(x, y):
        if x > y:
            largest = x
        else:
            largest = y
        while True:
            if (largest % x == 0) and (largest % y == 0):
                lcm = largest
                break
                largest = largest + 1
        return lcm

    num1 = int(input("please enter first num: "))
    num2 = int(input("please enter second num: "))
    result = lcm_of_num(2, 3)
    print("LCM of two number: ")
    print(result)


# Input a number and display that how many digits it has.
def problem64():
    num = int(input("please enter a number:"))
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    print("number of digits in a number: ", count)


# . Input a base-9 number, digit by digit, then convert it into decimal number. Digits
# ofthe input will be entered in order from least significant to most significant.
# Since valid digits are 0 to 8, hence any other input will be used as the sentinel
# value.
def problem65_and_66():
    data = int(input("Enter Numnaber :"))

    if "9" in str(data):
        print("not valid")
    else:
        x = [int(a) for a in str(data)]
        d = len(x) - 1
        new_list = []
        for element in x:
            new_list.append((pow(9, d) * element))
            d = d - 1

        print(sum(new_list))


# input a number and display its equivalent in base-9 (one digit per line, starting from the least significant)
def problem67():
    data = int(input("Enter Number :"))
    if "9" in str(data):
        print("not valid")
    else:
        pass
    # While the integer is greater than 0,
    decimal_value = ""
    while data > 0:
        decimal_value = str(data % 9) + decimal_value
        data //= 9
        print(decimal_value)


# nput number and store its equivalent in base-9 as a single numeric value
# anddisplay it.
def problem68():
    num = int(input("enter a number"))
    base = 9
    newNum = ''

    # While the integer is greater than 0,
    while num > 0:
        newNum = str(num % base) + newNum

        num //= base

    print(newNum)


# #nput a base-9 number, digit by digit, then convert it into binary number a single
# numeric value. Digits of the input will be entered in order from least significant to
# most significant. Since valid digits are 0 to 8, hence any other input will be used
# assentinel value
def problem69():
    data = int(input("Enter Number :"))

    if "9" in str(data):
        print("not valid")
    else:

        # convert to decimal
        decimal = int(str(data), base=9)

        base = 2
        newNum = ''

        # While the integer is greater than 0,
        while decimal > 0:
            newNum = str(decimal % base) + newNum

            decimal //= base

        print(newNum)


def problem70():
    def hexa(n):
        # n = input("entr nuber: ")
        hexa_num = ""
        while n != 0:
            temp = 0
            temp = n % 16
            if temp < 10:
                hexa_num = chr(temp + 48) + hexa_num
            else:
                hexa_num = chr(temp + 55) + hexa_num
            n = int(n / 16)
        print(hexa_num)

    n = 2545
    hexa(n)


# Three numbers denoted by the variables A, B and C are supplied as input data.
# Printthese three number in ascending order.
def problem71():
    num1 = int(input("Enter First number : "))
    num2 = int(input("Enter Second number : "))
    num3 = int(input("Enter Third number : "))
    if num1 < num2 and num1 < num3:
        if num2 < num3:
            x, y, z = num1, num2, num3
        else:
            x, y, z = num1, num3, num2
    elif num2 < num1 and num2 < num3:
        if num1 < num3:
            x, y, z = num2, num1, num3
        else:
            x, y, z = num2, num3, num1
    else:
        if num1 < num2:
            x, y, z = num3, num1, num2
        else:
            x, y, z = num3, num2, num1
    print("Numbers in ascending order are : ", x, y, z)


#  #Write an if-else statement that outputs the word “Warning” provided that either the
# value of the variable temperature is greater than or equal to 100, or the value of
# the variable pressure is greater than or equal to 200, or both. Otherwise, the if-else statement outputs the work “OK”.
def problem72():
    temp = int(input("Please enter value for temp: "))
    pressure = int(input("Please enter value for pressure: "))
    if temp >= 100 or pressure >= 200:
        print("warning")
    elif temp >= 100 and pressure >= 200:
        print("warning")
    else:
        print("OK")

# Input two positive integers and a and b from the user. Determine the integer of a/b
def problem73():
    num1 = int(input("please enter first num: "))
    num2 = int(input("please enter second num: "))
    result = 0
    div = num1 + num2
    while div > num2:
        div = div - num2
        result = result + 1
        print(result)


if __name__ == "__main__":
    problem26()
