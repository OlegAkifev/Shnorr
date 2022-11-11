from modules import power_mod, find_p_q
from random import randint


# Находим g такое что g^q = 1(modp). g = h^((p - 1)/q)(modp)
def gen_public_g(p, q):
    h = (randint(1, p - 1))
    g = power_mod(h, (p - 1) / q, p)
    return g


# Находим w из множества целых чисел такое что w < q
def gen_private_w(q):
    w = randint(10 ** 20, q - 1)
    return w


# Находим y = g^(g - w)(mod p)
def gen_public_y(g, w, p, q):
    y = power_mod(g, q - w, p)
    return y


# Создаем файл с открытыми ключами p, q, g, y
def create_file_with_public_keys(p, q, g, y):
    public_keys = [p, q, g, y]
    with open('file_with_public_keys', 'w') as file_with_public_keys:
        for key in public_keys:
            file_with_public_keys.writelines(str(key) + '\n')


# Создаем файл с закрытым ключом w
def create_file_with_private_key(w):
    with open('file_with_private_key', 'w') as file_with_private_key:
        file_with_private_key.write(str(w) + '\n')


def generation_keys():
    p, q = find_p_q()  # Генерируем простое p 512 бит и находим простое q, такое что p -1 = 0(modq)
    g = gen_public_g(p, q)
    w = gen_private_w(q)
    y = gen_public_y(g, w, p, q)
    create_file_with_public_keys(p, q, g, y)
    create_file_with_private_key(w)
    print(f'p = {p}\nq = {q}')
    print(f'g = {g}')
    print(f'w = {w}')
    print(f'y = {y}')
    print('Ключи сгенерированы')


generation_keys()
