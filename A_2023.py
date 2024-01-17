def solve():
    n,k = map(int, input().split())
    A = list(map(int, input().split()))
    C = 2023
    for a in A:
        if C%a != 0:
            print("No")
            return
        C //= a
    
    print("yes")
    print(C, end=" ")
    k -=1
    while k > 0:
        print("1", end=" ")
        k -=1
    print()




t = int(input())
while t>0:
    solve()
    t-=1

