#PYQ Endsem 
'''Write a Python function that takes a list of integers as input and returns a new list containing
only the even numbers from the original list'''

def filter_even_nums(numbers):
    even_numbers=[] #declare empty list
    for num in numbers:
        if num%2==0:
            even_numbers.append(num)
    return even_numbers
        
len=int(input("How many numbers do you want to enter? :"))
numbers=[] #declare empty list
for i in range (len):
    num=int(input(f"Enter number {i}: "))
    numbers.append(i)

even_numbers=filter_even_nums(numbers)
print(even_numbers)
