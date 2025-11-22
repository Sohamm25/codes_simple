# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# a = int(input("Enter a number: "))
# print(fibonacci(a))
# 0, 1, 1, 2, 3, 5, 8 
# def fib():
#     a = int(input("Enter:"))
#     def build_fib():
#         abc = [0, 1]  # Initialize the list with the first two Fibonacci numbers
#         for n in range(2, a):  # Start from index 2 since 0 and 1 are already there
#             next_value = abc[n - 1] + abc[n - 2]  # Calculate the next Fibonacci number
#             abc.append(next_value)  # Append the new number to the list
#         print("whole list==", abc)  # Print the Fibonacci sequence
#         print("last element =" abc[-1])
#     build_fib()
# fib()

def fib_memo(n, aaa={}):
    if n in aaa:  # Check if Fibonacci number is already cached
        return aaa[n]
    if n <= 1:  # Base cases
        return n
    aaa[n] = fib_memo(n - 1, aaa) + fib_memo(n - 2, aaa)
    return aaa[n]
a = int(input("Enter a number: "))
print(f"Fibonacci number at position {a} is {fib_memo(a)}")

