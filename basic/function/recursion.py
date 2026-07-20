# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)
# countdown(10)  


# ---fibonacci---
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n -1) + fibonacci( n -2)
# print(fibonacci(7))  # Output: 2        




# --------Recursion with Lists------------
# def sum_list(numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         return numbers[0] + sum_list(numbers[1:])

# my_list = [1, 2, 3, 4, 5]
# print(sum_list(my_list))

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        mx = find_max(numbers[1:])
        return numbers[0] if numbers[0] > mx else mx


my_numbers = [3, 7, 2, 9, 5,10]
print(find_max(my_numbers))  # Output: 9


