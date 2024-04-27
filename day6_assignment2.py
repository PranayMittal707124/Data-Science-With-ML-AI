# #Question 1
# def is_palindrome(s):
    
#     return s == s[::-1]

# a = input("enter a word.\n")
# print(is_palindrome(a))  
# #Question 2
# def calculator(num1, num2, operation):
#     if operation == 'add':
#         return num1 + num2
#     elif operation == 'subtract':
#         return num1 - num2
#     elif operation == 'multiply':
#         return num1 * num2
#     elif operation == 'divide':
#         if num2 == 0:
#             return "Error: Division by zero"
#         else:
#             return num1 / num2
#     else:
#         return "Error: Unsupported operation"
# x = int (input("enter frist number\n "))
# y = int (input("enter second number\n "))
# z = input("enter which operation do u add,subtract,multiply,divide\n")
# print(calculator(x,y,z))        
#Question 3
# def word_counter(S):
#     char_count = {}
#     S = S.replace(" ", "").lower()
#     for char in S:
#         char_count[char] = char_count.get(char, 0) + 1
#     for char, count in char_count.items():
#         print(f"{char} -> {count}")
# z = input("enter a word\n")
# word_counter(z)

# #Question 4
# def right_triangle_pattern(n):
#     for i in range(1, n + 1):
#         print('*' * i)
# x = int (input("enter frist number\n "))
# right_triangle_pattern(x)
# # Question 5
# def multiplication_table(n):
#     for i in range (1,11):
#         print(f"{n} x {i} = {n * i}")
# x = int (input("enter frist number\n "))
# multiplication_table(x)
