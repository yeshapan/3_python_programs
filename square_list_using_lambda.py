#PYQ Endsem 2023
'''Write a lambda function in Python called square_number that takes a number as input and
returns its square. Demonstrate the usage of this lambda function by squaring a list of numbers.
'''
#lambda function to square a num
square_num=lambda x:x**2

#use it to square all elements of a list
num_list=[1,2,3,4,5]
sqaured_list=list(map(square_num, num_list))

#print output to console
print("Original list: ", num_list)
print("Squared list: ", sqaured_list)

#output
'''
Original list:  [1, 2, 3, 4, 5]
Squared list:  [1, 4, 9, 16, 25]
'''
