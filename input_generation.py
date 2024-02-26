n = 4576

f = open("input.txt", "a")
f.write(str(n) + "\n")

for i in range(1, n):
    if i % 4 != 0:
        f.write(f"1 {i + 1}\n")
    else:
        f.write(f"1 {i - 3}\n")
