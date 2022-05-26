import random
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def print_m(M, tt):
    print(" время = " + str(tt) + " seconds.")
    for i in M:
        for j in i:
            print("%5d" % j, end=' ')

        print()




N = int(input("Введите N в интервале от 3 до 100:"))
while N < 3 or N > 100:
    row_q = int(input(
        "Вы ввели неверное число"))
K = int(input("Введите число К="))
start = time.time()

A = [[0] * N for i in range(N)]  # создание матрицы A
for i in range(N):
    for j in range(N):
        A[i][j] = random.randint(-10, 10)
print("A")
time_next = time.time()
print_m(A, time_next - start)


B = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы B
for i in range(int(len(A) // 2)):
    for j in range(int((len(A)) // 2)):
        B[i][j] = A[i][j]
print("B")
time_next = time.time()
print_m(B, time_next - start)


C = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы C
for i in range(int(len(A) // 2)):
    for j in range(int((len(A) + 1) // 2), len(A)):
        C[i][j - int((N + 1) / 2)] = A[i][j]
print("C")
time_next = time.time()
print_m(C, time_next - start)


E = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы E
for i in range((int(len(A) + 1) // 2), len(A)):
    for j in range(int((len(A) + 1) // 2), len(A)):
        E[i - int((N + 1) / 2)][j - int((N + 1) / 2)] = A[i][j]
print("E")
time_next = time.time()
print_m(E, time_next - start)


D = [[0] * int(N // 2) for i in range(N // 2)]  # создание матрицы D
for i in range(int(len(A) // 2), len(A)):
    for j in range(int((len(A)) // 2)):
        D[i - int((N + 1) / 2)][j] = A[i][j]
print("D")
time_next = time.time()
print_m(D, time_next - start)


F = [[0] * N for i in range(N)]  # Создание матрицы F равной A
for i in range(N):
    for j in range(N):
        F[i][j] = A[i][j]
print("F")
time_next = time.time()
print_m(F, time_next - start)

det= np.linalg.det(np.array(A))

s4et_1 = 0
s4et_2 = 0
for i in range(N // 2):
    for j in range(N // 2):
        if (j + i) % 2 == 0 and C[i][j] == 0:
            s4et_1 += 1


for i in C[0]:
    s4et_2 *= i
if len(C) > 1:
    for i in C[-1]:
        s4et_2 *= i
for i in range(1, N // 2 - 1):

    s4et_2 *= C[i][0]
    s4et_2 *= C[i][-1]

if s4et_1 > s4et_2: # если нет меняем  симетрично B и C
    for i in range(0, N // 2):
        for j in range(0, N // 2):
            F[i][j], F[i][-j -1] = F[i][-j - 1], F[i][j]
    print("F")
    time_next = time.time()
    print_m(F, time_next - start)

else: # если нет меняем не симетрично B и E
    for i in range(0, N // 2):
        for j in range(0, N // 2):
            F[i][j], F[i + N // 2][j + N // 2] = F[i + N // 2][j + N // 2], F[i][j]
    print("F")
    time_next = time.time()
    print_m(F, time_next - start)

diag = 0
for i in range(N):  # обрабатываем подматрицу C
        diag += F[i][-i - 1]
        diag += F[i][i]

if det > diag:
    print(np.dot(np.linalg.inv(A), (np.transpose(A)))-K*np.linalg.inv(F))
else:
    print((A+np.tril(A)-np.transpose(F))*K)

fig, ax = plt.subplots()                                #matplotlib
ax.set(xlabel='column number', ylabel='value')
for i in range(N):
    for j in range(N):
        plt.bar(i, a[i][j])
plt.show()

fig, ax = plt.subplots()
ax.set(xlabel='column number', ylabel='value')
ax.grid()
for j in range(N):
    ax.plot([i for i in range(N)], a[j][::])
plt.show()

ax = plt.figure().add_subplot(projection='3d')
ax.set(xlabel='x', ylabel='y', zlabel='z')
for i in range(N):
    plt.plot([j for j in range(N)], a[i][::], i)
plt.show()


sns.heatmap(data = F, annot = True)                 #seaborn
plt.xlabel('column number')
plt.ylabel('row number')
plt.show()

sns.boxplot(data = F)
plt.xlabel('column number')
plt.ylabel('value')
plt.show()

sns.lineplot(data = F)
plt.xlabel('column number')
plt.ylabel('value')
plt.show()
