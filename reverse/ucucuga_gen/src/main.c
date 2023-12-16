#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_SHIFT 128 // Максимальное случайное число для ключа

void encrypt(char *message, int key)
{
    int len = strlen(message);
    for (int i = 0; i < len; i++)
    {
        message[i] ^= key; // Применение XOR к каждому символу сообщения с ключом
    }
}

int main()
{
    srand(time(0)); // Инициализация генератора случайных чисел

    char message[100];
    printf("Enter your flag: ");
    fgets(message, sizeof(message), stdin);

    int key = rand() % MAX_SHIFT + 1; // Генерация случайного ключа от 1 до 100
    printf("Your key: %d\n", key);

    encrypt(message, key);
    printf("Your ucucuga: %s\n", message);

    return 0;
}
