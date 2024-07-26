def check_perfect_number(num):
    if num <= 0:
        return False
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

print(check_perfect_number(28))  
print(check_perfect_number(7))   