# Импортируем необходимые функции из библиотеки Crypto
from Crypto.Util.number import inverse

# Функция для нахождения простых множителей числа
def factor(num):
    result = []
    d = 2
    # Используем алгоритм деления на множители для нахождения множителей
    while d * d <= num:
        if num % d == 0:
            result.append(d)
            num //= d
        else:
            d += 1
    if num > 1:
        result.append(num)
    return result

# Функция для разбиения чисел на блоки
def blocking(num, size_num, size_block):
    return [int.from_bytes(num.to_bytes(size_num, 'big')[i * size_block: (i + 1) * size_block], 'big') for i in range(size_num // size_block)]

# Функция для дешифрования
def decrypt(C, d, n):
    bytes_val = blocking(C, 32, 4)
    res = bytearray()
    for num in bytes_val:
        # Используем последовательную операцию возведения в степень для дешифрования
        res += pow(num, d, n).to_bytes(8, 'big')
    return int.from_bytes(res, 'big')

# Функция для шифрования
def encrypt(P, e, n):
    bytes_val = blocking(P, 64, 8)
    res = bytearray()
    for num in bytes_val:
        # Используем последовательную операцию возведения в степень для шифрования
        res += pow(num, e, n).to_bytes(4, 'big')
    return int.from_bytes(res, 'big')

# Заданные значения
n = 517758144238469
e = 15931
C = 419529693641281414842251130008422950947927526

# Вывод зашифрованного текста
print('Зашифрованный текст:', C)

# Вычисление простых множителей для n
p, q = factor(n)
print('p =', p, ', q =', q)

# Вычисление значения (p-1)*(q-1)
f = (p - 1) * (q - 1)
print('f =', f)

# Вычисление секретного ключа
d = inverse(e, f)
print('d =', d)

# Расшифровка
P = decrypt(C, d, n)
print('Расшифрованный текст:', P)

# Шифрование для проверки
C = encrypt(P, e, n)
print('<Проверка> Зашифрованный текст:', C)
