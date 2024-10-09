#include <stdio.h>
#include <stdbool.h>

bool is_prime(long long num) {
    if (num <= 1) return false;
    if (num == 2 || num == 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    
    for (long long i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0)
            return false;
    }
    return true;
}

long long largest_prime_factor(long long n) {
    long long largest_factor = 1;
    long long factor = 2;

    // Check for smallest factors first
    while (factor * factor <= n) {
        if (n % factor == 0) {
            n /= factor;
            largest_factor = factor;
        } else {
            factor++;
        }
    }

    if (n > 1) { // The remaining number itself could be a prime factor
        largest_factor = n;
    }

    return largest_factor;
}

int main() {
    long long number;
    printf("enter a number: ");
    scanf("%lld",&number);
    printf("The largest prime factor is: %lld\n", largest_prime_factor(number));
    return 0;
}

