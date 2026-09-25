def matrix_chain(p):
    n = len(p) - 1

    # dp[i][j] stores minimum multiplication cost
    dp = [[0] * n for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):
                cost = (dp[i][k] +
                        dp[k + 1][j] +
                        p[i] * p[k + 1] * p[j])

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]



p = [10, 20, 30, 40, 30]

print("Minimum number of multiplications:", matrix_chain(p))
