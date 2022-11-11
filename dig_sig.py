from random import randint
import hashlib
from modules import power_mod


def digital_signature(name_of_file, file_with_private_key, file_with_public_keys, file_with_signature):
    with open(name_of_file, 'rb') as f:
        m = hashlib.sha1()
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
        hash_file = int(m.hexdigest(), 16)
    with open(file_with_private_key, 'r') as private_file:
        for elem in private_file:
            w = int(elem)
    numbers_public = []
    with open(file_with_public_keys, 'r') as public_file:
        for elem in public_file:
            numbers_public.append(int(elem))
    p, q, g, y = numbers_public[0], numbers_public[1], numbers_public[2], numbers_public[3]
    r = randint(10 ** 20, q - 1)
    x = power_mod(g, r, p)
    concatenation = str(hash_file) + str(x)
    concatenation_hash = hashlib.sha1(concatenation.encode())
    s1 = int(concatenation_hash.hexdigest(), 16)
    s2 = power_mod(r + (w * s1), 1, q)
    signature = [s1, s2]
    with open(file_with_signature, 'w') as file_with_signature:
        file_with_signature.write(name_of_file + '\n')
        for elem in signature:
            file_with_signature.writelines(str(elem) + '\n')
    return 'Файл подписан'


print(digital_signature('important_document', 'file_with_private_key', 'file_with_public_keys', 'signature'))



