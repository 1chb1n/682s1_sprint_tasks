import pandas as pd

# 1) 10, 20, 30, 40 elementlərindən ibarət s1 adlı series yaradın
s1 = pd.Series([10, 20, 30, 40])

# 2) s1-ə 'w', 'x', 'y', 'z' indekslərini təyin edin
s1.index = ['w', 'x', 'y', 'z']
print(s1)

# 3) {'p': 5, 'q': 10, 'r': 15} dictionary-dən s2 adlı Series yaradın
s2 = pd.Series({'p': 5, 'q': 10, 'r': 15})
print(s2)

# 4) s2-dən 'q' indeksli elementi seçin
print(s2['q'])

# 5) s1-dən 25-dən böyük elementləri seçin
print(s1[s1 > 25])

# 6) s1-də 20-dən böyük elementləri 10-a bölün 
print(s1[s1 > 20] / 10)

# 7) ((1, 2), (3, 4)) listindən df1 adlı dataframe yaradın
df1 = pd.DataFrame([[1, 2], [3, 4]])

# 8) df1-ə ('r1', 'r2') sətir və ('c1', 'c2') sütun adlarını təyin edin
df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']
print(df1)

# 9) {'A': [1, 2], 'B': [3, 4]} dictionary-dən df2 yaradın
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df2)

# 10) df2-də 'A' sütunu 1-dən böyük olan sətirləri seçin
print(df2[df2['A'] > 1])
