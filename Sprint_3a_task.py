# 1
x = int(input("x: "))
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

# 2
n = int(input("n: "))
if n % 2 == 0:
    print("cüt")
else:
    print("tək")

# 3
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("Ən böyük:", max(a, b, c))

# 4
day = int(input("day (1-7): "))
days = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print(days.get(day, "Yanlış gün"))

# 5
temp = int(input("Temperatur: "))
if temp < 0:
    print("soyuq")
elif 0 <= temp <= 20:
    print("normal")
else:
    print("isti")

# 6
password = input("Şifrə: ")
if len(password) < 8:
    print("qısa")
elif 8 <= len(password) <= 12:
    print("orta")
else:
    print("uzun")

# 7
x = int(input("x: "))
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

# 8
for i in range(0, 21, 2):
    print(i)

# 9
text = "Bağda ərik var idi …"
for char in text:
    print(char)

# 10
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# 11
i = 1
while True:
    if i % 5 == 0:
        print(i)
        break
    i += 1

# 12
lst = [1, 3, 5, 7, 9]
for idx, val in enumerate(lst):
    if val == 5:
        print("İndeks:", idx)
        break
