## Loops

# Exercise 1 
# Create multiplication table

# input1 = int(input("Enter a number: "))
# input2 = int(input("Enter a number to multiply by: "))

# # multiply
# for input1 in range(1, 20):
#     print(f"{input1} x {input2} = {input1 * input2}")

# exponential
# while input1 >= 0:
#     print(input1)
#     input1 = input1 * input2
#     if input1 >= 100:
#         break

## Prime numbers from input range
prime = int(input("Enter a number: "))

if prime > 1:
    for i in range(2, prime):
        if (prime % i) == 0:
            print(f"{prime} is not a prime number")
            break
    else:
        print(f"{prime} is a prime number")

# for prime in range(2, prime + 1):
#     for i in range(2, prime):
#         if (prime % i) == 0:
#             break
#     else:
#         print(f"{prime} is a prime number")