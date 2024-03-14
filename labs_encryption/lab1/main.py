import numpy as np

# generate inverse matrix by modulus
def get_inverse_matrix(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))

    # inverse number by modulus - two options 
    #det_inv = pow(det, -1, modulus)
    det_inv = extended_euclidean_algorithm(modulus, det)

    #print(det, '; ', det_inv)
    #print(matrix)
    
    inverse_matrix = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus

    #print(inverse_matrix)
    return inverse_matrix

def extended_euclidean_algorithm(a, b):
    u, v, A, B, C, D = a, b, 1, 0, 0, 1
    
    while v != 0:
        q = round(u / v)
        t1 = u - q * v
        t2 = A - q * C
        t3 = B - q * D
        
        u, A, B, v, C, D = v, C, D, t1, t2, t3
    
    d, x, y = u, A, B
    
    if y >= 0:
        inv = y
    else:
        inv = y + a
    
    return inv


def encrypt(text, key_matrix, modulus):
    # change register and expand to triad
    text = text.upper()
    while len(text) % 3 != 0:
        text += '*'
    
    # encrypt all blocks of three
    encrypted_text = ""
    for i in range(0, len(text), 3):
        block = np.array([[ord(c) - ord('A') if c != '*' else 26 for c in text[i:i+3]]])
        encrypted_block = np.dot(block, key_matrix) % modulus
        encrypted_text += ''.join([chr(num + ord('A')) if num != 26 else '*' for num in encrypted_block.flatten()])
    return encrypted_text


def decrypt(encrypted_text, key_matrix, modulus):
    # decrypt all blocks of three
    decrypted_text = ""
    for i in range(0, len(encrypted_text), 3):
        block = np.array([[ord(c) - ord('A') if c != '*' else 26 for c in encrypted_text[i:i+3]]])
        decrypted_block = np.dot(block, get_inverse_matrix(key_matrix, modulus)) % modulus
        decrypted_text += ''.join([chr(num + ord('A')) if num != 26 else '*' for num in decrypted_block.flatten()])
    return decrypted_text

# main
plaintext = "HELLO"
key_matrix = np.array([[3, 2, 5], [1, 4, 7], [2, 0, 1]])  
modulus = 29  # prime number


encrypted_text = encrypt(plaintext, key_matrix, modulus)
print("Enrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key_matrix, modulus)
print("Decrypted text:", decrypted_text)
