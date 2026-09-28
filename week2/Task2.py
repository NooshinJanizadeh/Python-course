def sum_and_average_of_digits(s1):
    digits = [int(char) for char in s1 if char.isdigit()]
    if not digits:
        return 0, 0
    return sum(digits), sum(digits) / len(digits)

s1 = "Hello123World45"
print("Task 2:", sum_and_average_of_digits(s1))
