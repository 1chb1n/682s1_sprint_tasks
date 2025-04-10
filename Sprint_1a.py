# 1) 123 rəqəmini string/character ə çevirin və tipini yoxlayın.
num = 123
num_str = str(num)
print(num_str, type(num_str))

# 2) 19.99 dəyərini tam ədədə çevirin və nəticəni çap edin.
value = 19.99
int_value = int(value)
print(int_value)

# 3) "500" dəyərini numericə çevirin və 2-yə bölüb nəticəni çap edin.
val_str = "500"
val_num = int(val_str)
print(val_num / 2)

# 4) a = 8 və b = 12 yaradın. a < b və a == b şərtlərini yoxlayın, nəticələri çap edin.
a = 8
b = 12
print(a < b)
print(a == b)

# 5) x = 5, y = 10, z = 15 yaradın. (x < y) and (y < z) şərtini yoxlayın və nəticəni çap edin.
x = 5
y = 10
z = 15
print((x < y) and (y < z))

# 6) 25-i 4-ə bölün. Tam bölmə, qalıq və adi bölmə nəticələrini çap edin.
print(25 // 4)  # tam bölmə
print(25 % 4)   # qalıq
print(25 / 4)   # adi bölmə

# 7) 3-ü 4-cü dərəcəyə qaldırın və nəticəni çap edin.
print(3 ** 4)

# 8) qiymet = 75.5 yaradın. Onu tam ədədə çevirin və tipini yoxlayın.
qiymet = 75.5
qiymet_int = int(qiymet)
print(qiymet_int, type(qiymet_int))

# 9) n = 20 yaradın. (n > 10) or (n < 5) və (n > 15) and (n < 25) şərtlərini yoxlayın, nəticələri çap edin.
n = 20
print((n > 10) or (n < 5))
print((n > 15) and (n < 25))

# 10) "42.8" dəyərini əvvəl float-a, sonra tam ədədə çevirin və hər addımda tipi yoxlayın.
s = "42.8"
f = float(s)
print(f, type(f))
i = int(f)
print(i, type(i))
