def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-10 + 1):  # Fixed the range to include n-10
            out *= i
    else:
        lim = n - 20
        out = lim * (lim + 1) // 2  # Fixed the calculation of the sum
    print(out)

n = int(input("Enter an integer: "))
compute(n)