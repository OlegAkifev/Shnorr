from Cryptodome.Util import number
import random
import math


def egcd(c, d):
    if c == 0:
        return d, 0, 1
    else:
        g, x, y = egcd(d % c, c)
        return g, y - (d // c) * x, x


# Ищем обратный элемент в кольце по модулю
def find_inverse_elem(k, p):
    g, x, _ = egcd(k, p)
    if g == 1:
        return x % p


# НОД
def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


# Возведение в степень по модулю
def power_mod(b, e, m):
    x = 1
    while e > 0:
        if e % 2:
            b, e, x = (b * b) % m, e // 2, (b * x) % m
        else:
            b, e, x = (b * b) % m, e // 2, x

    return x


def is_fermat_probable_prime(n, *, trials=32):
    import random
    if n <= 16:
        return n in (2, 3, 5, 7, 11, 13)
    for i in range(trials):
        if power_mod(random.randint(2, n - 2), n - 1, n) != 1:
            return False
    return True


def pollard_rho_factor(N, *, trials=16):
    for j in range(trials):
        i, stage, y, x = 0, 2, 1, random.randint(1, N - 2)
        while True:
            r = math.gcd(N, x - y)
            if r != 1:
                break
            if i == stage:
                y = x
                stage <<= 1
            x = (x * x + 1) % N
            i += 1
        if r != N:
            return [r, N // r]
    return [N]  # Pollard-Rho failed


def trial_division_factor(n, *, limit=None):
    fs = []
    while n & 1 == 0:
        fs.append(2)
        n >>= 1
    d = 3
    while d * d <= n and limit is None or d <= limit:
        q, r = divmod(n, d)
        if r == 0:
            fs.append(d)
            n = q
        else:
            d += 2
    if n > 1:
        fs.append(n)
    return fs


def factor(n):
    if n <= 1:
        return []
    if number.isPrime(n) == 1:
        return [n]
    fs = trial_division_factor(n, limit=1 << 12)
    if len(fs) >= 2:
        return sorted(fs[:-1] + factor(fs[-1]))
    fs = pollard_rho_factor(n)
    if len(fs) >= 2:
        return sorted([e1 for e0 in fs for e1 in factor(e0)])
    return trial_division_factor(n)


def find_p_q():
    n = number.getPrime(512) - 1
    fs = factor(n)
    return n + 1, fs[-1]


if __name__ == '__main__':
    print(find_p_q())
