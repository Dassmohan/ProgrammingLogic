x = input()
y = int(input())
z = []
for i in range(0, len(x), y):
    z.append(x[i:i+y])
for a in z:
    print(a)
