#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void vuln(char *input)
{
    char buffer[16];
    int secret_value = 0xDEAD; // Значение, которое мы хотим перезаписать

    strcpy(buffer, input); // Уязвимое копирование данных без проверки длины

    printf("Your buffer: %s", buffer);

    if (secret_value == 1337)
    {
        printf("Your flag: %s", getenv("FLAG"));
    }
}

int main()
{
    char input[24];
    printf("Enter your input: ");
    scanf("%s", input);

    vuln(input);

    return 0;
}
