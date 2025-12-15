#Task 1
print("Введіть число(додатне): ")
n = abs(int(input())) 
s = 0

while n > 0:
    s += n % 10
    n //= 10
print("Сума чисел: ")
print(s)
#Task 2
print("Введіть число: ")
n = int(input())
count = 0

for i in range(1, n + 1):
    if str(i) == str(i)[::-1]:
        count += 1
print("Кількість чисел-паліндромів: ")
print(count)
#Task 3
print("Введіть текст: ")
s = input()

clean = ''
for ch in s:
    if ch.isalpha():
        clean += ch
    else:
        clean += ' '

words = clean.split()

max_word = words[0]
for w in words:
    if len(w) > len(max_word):
        max_word = w
print("Найдовше слово: ")
print(max_word.capitalize())
