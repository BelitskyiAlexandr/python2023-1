import numpy as np

# Функція для генерації оберненої матриці за допомогою розширеного алгоритму Евкліда
def get_inverse_matrix(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)

    # Знаходимо обернену матрицю
    inverse_matrix = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    print(inverse_matrix)
    return inverse_matrix

# Функція для шифрування тексту за допомогою методу Лестера Хілла
def encrypt(text, key_matrix, modulus):
    # Змінюємо регістр символів та додаємо символи до тексту до кратності 3
    text = text.upper()
    while len(text) % 3 != 0:
        text += '*'
    
    # Поділяємо текст на блоки по три символи та шифруємо кожен блок
    encrypted_text = ""
    for i in range(0, len(text), 3):
        block = np.array([[ord(c) - ord('A') if c != '*' else 26 for c in text[i:i+3]]])
        encrypted_block = np.dot(block, key_matrix) % modulus
        encrypted_text += ''.join([chr(num + ord('A')) if num != 26 else '*' for num in encrypted_block.flatten()])
    return encrypted_text

# Функція для дешифрування тексту за допомогою методу Лестера Хілла
def decrypt(encrypted_text, key_matrix, modulus):
    # Поділяємо текст на блоки по три символи та дешифруємо кожен блок
    decrypted_text = ""
    for i in range(0, len(encrypted_text), 3):
        block = np.array([[ord(c) - ord('A') if c != '*' else 26 for c in encrypted_text[i:i+3]]])
        decrypted_block = np.dot(block, get_inverse_matrix(key_matrix, modulus)) % modulus
        decrypted_text += ''.join([chr(num + ord('A')) if num != 26 else '*' for num in decrypted_block.flatten()])
    return decrypted_text

# Приклад використання
plaintext = "HELLO"
key_matrix = np.array([[3, 2, 5], [1, 4, 7], [2, 0, 1]])  # Приклад ключа
modulus = 29  # Розмір алфавіту

# Шифруємо та дешифруємо текст
encrypted_text = encrypt(plaintext, key_matrix, modulus)
print("Зашифрований текст:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key_matrix, modulus)
print("Дешифрований текст:", decrypted_text)
