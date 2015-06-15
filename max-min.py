def max_min(array, n, k):
    array = sorted(array)
    return min(array[a+k-1]-array[a] for a in range(n - k + 1))

N = int(raw_input().strip())
K = int(raw_input().strip())

N_list = []
for _ in range(N):
    N_list.append(int(raw_input().strip()))

print max_min(N_list, N, K)
