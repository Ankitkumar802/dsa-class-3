# def ex_function(n, a):
#     result = 0
    
#     for i in range(n):
#         result += i
#         for j in range(n, n+2):
#             result += j
#             for k in range(n):
#                 result += k
#                 for l in range(a):
#                     result += l

    
#     return result
    
# print(ex_function(23,3)) 

# def open_file():
#     file = open("test.txt", "r")
    
#     file.close()
    
# print(file)



def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n]
print(fibonacci_dp(3))



