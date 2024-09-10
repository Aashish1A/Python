def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    """Print the first n prime numbers."""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1

# Input: Number of prime numbers to print
n = int(input("Enter the number of prime numbers to print: "))
print_first_n_primes(n)
