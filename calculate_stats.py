#PYQ Endsem 2023
'''Write a Python function called calculate_stats that takes a list of numbers as input and returns
three values: the sum, average, and maximum value of the input numbers.'''

def calculate_stats(numbers):
    #check if list  is empty
    if not numbers:
        sum_num=0
        avg=0
        max_num=None
    #if list not empty (use built-in list functions)
    sum_num=sum(numbers)
    avg=sum_num/len(numbers)
    max_num=max(numbers)
    print(f"Sum: {sum} , Average: {avg} , Max number: {max_num}")
