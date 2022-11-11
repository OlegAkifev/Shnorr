import hashlib
from modules import power_mod


def verification(signature, file_with_public_keys):
    numbers_public = []
    with open(file_with_public_keys, 'r') as public_file:
        for elem in public_file:
            numbers_public.append(int(elem))
    p, q, g, y = numbers_public[0], numbers_public[1], numbers_public[2], numbers_public[3]
    with open(signature, 'r', encoding='UTF-8') as signature:
        file = signature.readlines()[0].replace('\n', '')
        signature.seek(0)
        s1 = int(signature.readlines()[1])
        signature.seek(0)
        s2 = int(signature.readlines()[2])
    with open(file, 'rb') as f:
        m = hashlib.sha1()
        while True:
            data = f.read(1024)
            if not data:
                break
            m.update(data)
        hash_file = int(m.hexdigest(), 16)
    X = power_mod((power_mod(g, s2, p) * power_mod(y, s1, p)), 1, p)
    concatenation = str(hash_file) + str(X)
    concatenation_hash = hashlib.sha1(concatenation.encode())
    s = int(concatenation_hash.hexdigest(), 16)
    if s1 == s:
        print(f'Файл не изменялся\n{s1} = {s}')
    else:
        print(f'Файл изменялся\n{s1} != {s}')


verification('signature', 'file_with_public_keys')
