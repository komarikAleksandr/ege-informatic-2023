#include <iostream>
using namespace std;
void replaceMaxWithAverage(int arr[], int size) {

    int maxElement = arr[0];
    for (int i = 1; i < size; ++i) {
        if (arr[i] > maxElement) {
            maxElement = arr[i];
        }
    }

    int sumPositive = 0;
    int countPositive = 0;
    for (int i = 0; i < size; ++i) {
        if (arr[i] > 0) {
            sumPositive += arr[i];
            ++countPositive;
        }
    }

    if (countPositive > 0) {
        int average = sumPositive / countPositive;
        for (int i = 0; i < size; ++i) {
            if (arr[i] == maxElement) {
                arr[i] = average;
                break;
            }
        }
    }
}

void printArray(const int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main() {

    int X1[1] = {2};
    int X2[2] = {30, 40};
    int X3[3] = {-3, -4, -5};
    
    int sizeX1N1 = sizeof(X1) / sizeof(X1[0]);
    int sizeX2N2 = sizeof(X2) / sizeof(X2[0]);
    int sizeX3N3 = sizeof(X3) / sizeof(X3[0]);


    std::cout << "Massive before:" << std::endl;
    std::cout << "X1: ";
    printArray(X1, sizeX1N1);
    std::cout << "X2: ";
    printArray(X2, sizeX2N2);
    std::cout << "X3: ";
    printArray(X3, sizeX3N3);
    
    replaceMaxWithAverage(X1, sizeX1N1);
    replaceMaxWithAverage(X2, sizeX2N2);
    replaceMaxWithAverage(X3, sizeX3N3);
    
    std::cout << "Massive after:" << std::endl;
    std::cout << "X1: ";
    printArray(X1, sizeX1N1);
    std::cout << "X2: ";
    printArray(X2, sizeX2N2);
    std::cout << "X3: ";
    printArray(X3, sizeX3N3);

    return 0;
}