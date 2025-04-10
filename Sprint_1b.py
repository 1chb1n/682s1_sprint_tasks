# 1) s = "Programming" yaradın. Uzunluğunu və ilk simvolunu çap edin.
s = "Programming"
print(len(s))     # Uzunluq
print(s[0])       # İlk simvol

# 2) s1 = "Hello" və s2 = "World" yaradın. Onları boşluqla birləşdirin və nəticəni çap edin.
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

# 3) text = "Python" yaradın. Son simvolunu çap edin.
text = "Python"
print(text[-1])

# 4) s = "Artificial" yaradın. "Art" hissəsini ilə çıxarın və çap edin.
s = "Artificial"
print(s[3:])   # 4-cü simvoldan sonrakı hissə (yəni "ificial")

# 5) word = "Code" yaradın. Tərsinə çevirin və nəticəni çap edin.
word = "Code"
print(word[::-1])

# 6) s = "abcdefgh" yaradın. Hər ikinci simvolu alın və çap edin.
s = "abcdefgh"
print(s[0::2])

# 7) text = "data" yaradın. Onu bir sətrlik kodla böyük hərflərə və kiçik hərflərə çevirib çap edin.
text = "data"
print(text.upper(), text.lower())

# 8) s = "Python-R-Java" yaradın. "-" ilə ayırın (split("-")) və nəticəni çap edin.
s = "Python-R-Java"
print(s.split("-"))

# 9) ad = "Ayxan" və yaş = 25 yaradın. f-string ilə "Ayxan 25 yaşındadır" çap edin.
ad = "Ayxan"
yas = 25
print(f"{ad} {yas} yaşındadır")

# 10) s = "salam-dunya" yaradın. "-"ni boşluqla əvəz edin və nəticəni çap edin.
s = "salam-dunya"
print(s.replace("-", " "))
