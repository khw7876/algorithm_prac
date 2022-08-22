H,M = map(lambda x : int(x) , input().split())
M -= 45
if M < 0:
    H -= 1
    M += 60
if H < 0:
    H = 23
print(H,M)
