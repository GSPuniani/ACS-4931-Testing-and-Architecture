# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def calculate_mean(grades):
    total = 0
    for grade in grades:
        total += grade
    return 1.0 * total / len(grades)

def calculate_std(grades, mean):
    sum_of_sqrs = 0
    for grade in grades:
        sum_of_sqrs += (grade - mean) ** 2
    return math.sqrt(sum_of_sqrs / len(grades))


def print_stat():
    grade_list = []
    # Get the inputs from the user
    NUM_STUDENTS = 5
    for _ in range(NUM_STUDENTS):
        grade_list.append(int(input('Enter a number: ')))

    # Calculate the mean and standard deviation of the grades
    mean = calculate_mean(grade_list)
    std = calculate_std(grade_list, mean)
    
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(std, 3))
    print('****** END ******')

print_stat()
