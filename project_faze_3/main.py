def maximize_profit(n, x, Cs, S, Cb, B):
    dp = [0] * (n + 1)
    for t in range(n + 1):
        dp[t] += x
        if t + 1 <= n:
            dp[t + 1] = max(dp[t + 1], dp[t])
        if t + 1 <= n and dp[t] >= Cs[t]:
            dp[t + 1] = max(dp[t + 1], dp[t] - Cs[t] + Cs[t] * S[t])
        if t + 6 <= n and dp[t] >= Cb[t]:
            dp[t + 6] = max(dp[t + 6], dp[t] - Cb[t] + Cb[t] * B[t])
    return dp


# for manual test
# n = 10
# x = 100
# Cs = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# S = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
# Cb = [50, 52, 54, 56, 58, 60, 62, 64, 66, 68]
# B = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4]
# -------------------------------------------------------
# n = 3
# x = 100
# Cs = [20, 20, 20]
# S = [2, 2, 2]
# Cb = [50, 50, 50]
# B = [1.5, 1.5, 1.5]
# -------------------------------------------------------
n = int(input("number of months : "))
x = float(input("monthly income : "))
Cs = list(map(float, input("Course costs")))
S = list(map(float, input("Course profit rates")))
Cb = list(map(float, input("market costs")))
B = list(map(float, input("market profit rates")))
print(maximize_profit(n, x, Cs, S, Cb, B)[n])
