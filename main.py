"""
Ali Alzamani
"""
import math


def print_table_kg_lb():
    """
    A function to convert weights (30 - 100) from kg to lb
    First variant: no parameter, no return
    """
    for weight_kg in range(30, 101, 10):
        weight_lb = weight_kg * 2.20
        if weight_kg != 100:
            print(f"weight in kilos:    {weight_kg}    is    {weight_lb:.2f} in pounds")
        else:
            print(f"weight in kilos:   {weight_kg}    is    {weight_lb:.2f} in pounds")


def get_numbers_print_divisible():
    """
    the function prompts the user to enter three numbers, first number, second number and divisor.
    - If the first number is less than the second number then the
    function will display all the numbers between first and second
    number inclusive that are divisible by the given divisor.
    - If first number was greater than second number then the
    function will display all the numbers between the first and the
    second number that are divisible by the given divisor in descending order.
    - The divisor cannot be 0. If the divisor was 0 the message “the
    divisor cannot be 0” will be displayed and the function will terminate
    First variant: no parameter, no return
    """
    first_number = int(input("enter the first number: "))
    second_number = int(input("enter the second number: "))
    divisor = int(input("enter the divisor: "))
    if divisor == 0:
        print("the divisor cannot be 0")
        return
    if first_number < second_number:
        for number in range(first_number, second_number+1):
            if number % divisor == 0:
                print(number, end=" ")
    elif first_number > second_number:
        for number in range(first_number, second_number-1, -1):
            if number % divisor == 0:
                print(number, end=" ")


def get_numbers_print_analysis():
    """
    The function prompts the user to enter positive integers, space to end the input . If the user
    entered anything other than an integer or space, it will be ignored. If the user entered an integer it will be
    added to a list. The function displays the list of integers, the length of the list, number of even numbers,
    min and max numbers.
    First variant: no parameter, no return
    """
    input_integers = ""
    positive_integers = []
    while input_integers != " ":
        input_integers = input("enter positive integer: ")
        if input_integers.isspace():
            break
        elif input_integers.isdecimal():
            positive_integers.append(int(input_integers))
        else:
            print("you entered a non-integer input. Try again")
            continue
    print(f"\n{positive_integers}\n")
    print("the number of positive integers entered is: ", len(positive_integers), "\n")
    positive_integers_even = []
    for positive_integer in positive_integers:
        positive_integers_even.append(positive_integer)
    for positive_integer in positive_integers_even:
        if positive_integer % 2 != 0:
            positive_integers_even.remove(positive_integer)
    print("the number of even integers is: ", len(positive_integers_even), "\n")
    minimum = maximum = positive_integers[0]
    for positive_integer in positive_integers[1:]:
        if positive_integer < minimum:
            minimum = positive_integer
        else:
            if positive_integer > maximum:
                maximum = positive_integer
    print("the minimum is %d" % minimum)
    print("\nthe maximum is %d" % maximum)


def calculate_total_pay_usd(number_of_employees: int, hourly_rate_usd: float):
    """
    The function takes two parameters: number of employees and hourly rate in USD. The function displays the number of
    hours and the pay of each employee.
    Second variant: parameters, no return
    :param number_of_employees: number of employees
    :param hourly_rate_usd: hourly rate in USD.
    """
    overtime_hours_pay = hourly_rate_usd * 1.5
    for index in range(number_of_employees):
        hours_worked = int(input("enter the number of worked hours: "))
        employee = [hours_worked]
        if hours_worked <= 40:
            employee_pay_usd = hours_worked * hourly_rate_usd
            employee.append(employee_pay_usd)
        else:
            overtime_hours = hours_worked - 40
            employee_pay_usd = 40 * hourly_rate_usd + overtime_hours * overtime_hours_pay
            employee.append(employee_pay_usd)
        if index == 0:
            employees = [employee]
        else:
            employees.append(employee)
    for employee in employees:
        print("the employee worked for %d hours and earned %.2f $" % (employee[0], employee[1]))


def is_prime(positive_number: int):
    """
    the function takes one parameter which is a positive
    number and returns True if the number was prime, False otherwise
    Fourth variant: parameter and return
    :param positive_number: positive_number
    :return: True or False
    """
    for number in range(2, int(math.sqrt(positive_number)) + 1):
        if positive_number == 2:
            return True
        elif positive_number % number == 0:
            return False
    return True


def display_prime_numbers_to(maximum):
    """
    The function takes one argument which is a positive integer greater than 2, the function generates a
    list of integers from 2 to the given number inclusive. The function then
    iterates through the list and displays all the prime numbers in the list.
    Second variant: parameters, no return
    :param maximum: a positive integer greater than 2
    """
    for number in range(2, maximum+1):
        if is_prime(number):
            print("the number %d is prime number" % number)


def main():
    print_table_kg_lb()
    print("--------------------------------------")
    get_numbers_print_divisible()
    print("\n--------------------------------------")
    get_numbers_print_analysis()
    print("\n--------------------------------------")
    number_of_employees = int(input("enter the number of employees: "))
    hourly_rate = float(input("enter the hourly rate: "))
    calculate_total_pay_usd(number_of_employees, hourly_rate)
    print("\n--------------------------------------")
    maximum = int(input("enter a positive integer that is greater than 2: "))
    display_prime_numbers_to(maximum)


if __name__ == '__main__':
    main()
