##################################### LESSON 20 ##################################### 
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)



if __name__=='__main__':
    print(fib(4))


##################################### EXCERCISE 1 #####################################


def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])

print(list_sum([2, 4, 5, 6, 7]))


##################################### EXCERCISE 2 #####################################

def to_string(n, base):
    conver_tString = "0123456789ABCDEF"
    if n < base:
        return conver_tString[n]
    else:
        return to_string(n // base, base) + conver_tString[n % base]

print(to_string(2835, 16))


##################################### EXCERCISE 3 #####################################


def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element

    return total

print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))

##################################### EXCERCISE 4 #####################################


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

##################################### EXCERCISE 5 #####################################

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))


##################################### EXCERCISE 6 #####################################


def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(int(n / 10))
print(sumDigits(345))
print(sumDigits(45))



##################################### EXCERCISE 7 #####################################


def sum_series(n):
    if n < 1:
        return 0
    else:
        return n + sum_series(n - 2)
print(sum_series(6))
print(sum_series(10))


##################################### EXCERCISE 8 #####################################



def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)
print(harmonic_sum(7))
print(harmonic_sum(4))


##################################### EXCERCISE 9 #####################################


def geometric_sum(n):
    if n == 0:
        return 1
    else:
        return 1 / (pow(2, n)) + geometric_sum(n - 1)
print(geometric_sum(7))
print(geometric_sum(4))


##################################### EXCERCISE 10 #####################################


def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)
print(power(3, 4))



##################################### EXCERCISE 11 #####################################

def Recurgcd(a, b):
    low = min(a, b)
    high = max(a, b)
    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return Recurgcd(low, high % low)
print(Recurgcd(12, 14))
