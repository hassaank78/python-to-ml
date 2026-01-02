import math

def mean(list_of_num):
    sum = 0
    list_length = len(list_of_num)
    for num in list_of_num:
        sum += num
    return sum // list_length

def median(list_of_num):
    list_length = len(list_of_num)
    sorted_list = sorted(list_of_num)
    if list_length % 2 == 0:
        return (sorted_list[list_length // 2] + sorted_list[(list_length // 2) + 1])/2 
    return sorted_list[(list_length // 2)]

def std(list_of_num):
    my_mean = mean(list_of_num)
    print(my_mean)
    squared_deviations = [(x-my_mean)**2 for x in list_of_num]
    sum = 0
    for num in squared_deviations:
        sum += num
    return math.sqrt(sum / len(list_of_num))

input_string = input('Enter a list of numbers and only numbers separated with spaces')
try:
    input_arr = [float(x) for x in input_string.split(' ')]
    if input_arr == []:
        raise ValueError
    elif len(input_arr) == 1:
        raise ValueError
except ValueError:
    print('Invalid input. Please enter only numbers separated by spaces.')
    exit(1)

print(f'Mean: {mean(input_arr)}')
print(f'Median: {median(input_arr)}')
print(f'Standard Deviation: {std(input_arr)}')
