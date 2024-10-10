def fibNaive(n):
    if n <= 2:
        return 1;
    return fibNaive(n-1) + fibNaive(n-2)


def fibOptimized(n, memo={}):  # memo can be initialized by default so much easier :)
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1;

    memo[n] = fibOptimized(n-1, memo) + fibOptimized(n-2, memo)
    return memo[n];


n = 20;
print("\t>>>>nth Fibonacci Number Python Implementation<<<<")
print("Naive Algorithm:     n=", n, fibNaive(n))
print("Optimized Algorithm: n=", n, fibOptimized(n))