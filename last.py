import numpy as np
#Task 1
B = np.array([4,0,6,17,3,10,11,2,0,6,0])
non_zero = B[B != 0]      
zeros = B[B == 0]         
C = np.concatenate((non_zero, zeros))
print(C)
#Task 2
import numpy as np

data = ["a" * i for i in range(1, 10)]

np.savetxt("output.txt", data, fmt="%s")
#Task 3
import matplotlib.pyplot as plt

vowels = "аеєиіїоуюя"

freq = {v: 0 for v in vowels}

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

for char in text:
    if char in vowels:
        freq[char] += 1

letters = list(freq.keys())
counts = list(freq.values())

plt.bar(letters, counts)
plt.xlabel("Голосні літери")
plt.ylabel("Частота")
plt.title("Частота появи голосних літер у тексті")

plt.savefig("histogram.png")
plt.close()

print("Гістограму збережено у файл histogram.png")
#Task 4
A = np.array([2, 4, 6, 8])
B = np.array([1, 3, 5, 7])

print("Масив A:", A)
print("Масив B:", B)
print()

print("A + B =", A + B, "  # поелементне додавання")
print("A - B =", A - B, "  # поелементне віднімання")
print("A * B =", A * B, "  # поелементне множення")
print("A / B =", A / B, "  # поелементне ділення")
print()

C = np.concatenate((A, B))
print("Новий масив C (об’єднання A і B):", C)
print()

print("Максимальний елемент масиву C:", np.max(C))
print("Мінімальний елемент масиву C:", np.min(C))
print("Сума всіх елементів масиву C:", np.sum(C))
print("Добуток всіх елементів масиву C:", np.prod(C))