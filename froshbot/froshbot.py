#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_armstrong_number(int number) {
    int originalNumber = number;
    int numDigits = 0;
    
    while (number > 0) {
        number /= 10;
        numDigits++;
    }
    
    number = originalNumber;
    int sumOfPowers = 0;
    
    while (number > 0) {
        int digit = number % 10;
        sumOfPowers += pow(digit, numDigits);
        number /= 10;
    }
    
    return sumOfPowers == originalNumber;
}

int main() {
    int inputNumber;
    printf("Enter a number: ");
    
    if (scanf("%d", &inputNumber) == 1) {
        if (is_armstrong_number(inputNumber)) {
            printf("%d is an Armstrong number.\n", inputNumber);
        } else {
            printf("%d is not an Armstrong number.\n", inputNumber);
        }
    } else {
        printf("Invalid input. Please enter a valid number.\n");
    }
    
    return 0;
}