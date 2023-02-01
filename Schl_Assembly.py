N = int(input())
l = []
clk = 0
for i in range(N):
    t = int(input())
    l.append(t)
print(l)
for i in range(N):
    if (l[i] < N):
        clk = clk + 1
    elif (l[i] > N):
        break
    elif (l[i] == N):
        clk = clk + 1
        break
print(clk)
