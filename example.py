from Cryptodome.Util import number
from modules import power_mod, egcd
from random import randint
import hashlib
import math
# p = 772707662161
# q = 72103
#
# h = int(randint(1, p - 1))
# print(h)
#
# g = power_mod(h, (p - 1) / q, p)
# print(g)
#
# print((g ** q) % p)

message = '1235454353453453456'
#
# # Ключи
p = 205906154062598848791881958537459269003
q = 4923864222645723104688936786490489
h = 37476210401930915750216818118385774129021049737058300111377124815037597406065
g = 204920359083026328617888546106505150870
w = 4229382484668395269584420038459523
y = 191358353983226297528539277813303203866
#
# # Подпись
r = 43288306094299697014308
x = power_mod(g, r, p)
concat_1 = str(message) + str(x)
# print(concat_1)
concat_1_hash = hashlib.sha1(concat_1.encode())
s1 = int(concat_1_hash.hexdigest(), 36)
print(s1)
s2 = r + power_mod(w * s1, 1, q)
print(s2)

# # Проверка

x = power_mod(power_mod(g, s2, p) * power_mod(y, s1, p), 1, p)
print(x)

concat_2 = str(message) + str(x)
print(concat_2)
concat_2_hash = hashlib.sha1(concat_2.encode())
qwe = int(concat_2_hash.hexdigest(), 32)
print(qwe)
print(qwe, s1)
#
#


