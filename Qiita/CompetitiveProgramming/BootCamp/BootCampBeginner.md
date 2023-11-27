
## 1. Power Socket

https://atcoder.jp/contests/abc139/tasks/abc139_b

<details><summary>ポイント</summary>

A個口の電源タップの数-電源タップに使われている差し込み口の数。
B=1の場合は電源タップの必要がないことに注意。

</details>
<br>

所要時間: 4分45秒

<details><summary>解答コード</summary>


```python
def main():
    A, B = map(int, input().split())
    if B == 1:
        return 0
    for i in range(1, 20):
        if A*i-(i-1) >= B:
            return i

print(main())

```
</details>

## 2. Rally

https://atcoder.jp/contests/abc156/tasks/abc156_c


<details><summary>ポイント</summary>

座標のリストはソートされて与えられているわけではないことに注意して全探索。

</details>
<br>

所要時間: 4分37秒

<details><summary>解答コード</summary>


```python

def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10**18
    for meeting_place in range(max(X)+1):
        power_needed = 0
        for person in range(N):
            power_needed += (X[person] - meeting_place)**2
            
        ans = min(ans, power_needed)
    
    print(ans)

main()

```
</details>


## 3. Qualification Simulator 

https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b

<details><summary>ポイント</summary>

予選通過確定者と海外学生順位の二つの変数を保持しておいて上から都度確認。

</details>

<br>

所要時間: 5分15秒

<details><summary>解答コード</summary>


```python


def main():
    N, A, B = map(int, input().split())
    S = list(input())

    confirmed = 0
    foreign_rank = 0

    for participant in S:
        if participant == "a":
            if confirmed < A+B:
                print("Yes")
                confirmed += 1
            else:
                print("No")
        elif participant == "b":
            if confirmed < A+B and foreign_rank < B:
                print("Yes")
                confirmed += 1
                foreign_rank += 1
            else:
                print("No")
                foreign_rank += 1 
        else:
            print("No")
    
    return 

main()

```
</details>

## 4. Tax Rate

https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

<details><summary>ポイント</summary>

Pythonで小数を用いた掛け算、割り算をすると型が`float`型になってしまうことに注意する。念のため予想価格周り20円くらいも走査しておいた。

</details>
<br>

所要時間: 3分02秒

<details><summary>解答コード</summary>


```python
def main():
    N = int(input())
    possible_price = int(N // 1.08)

    for price in range(possible_price-20, possible_price+21):
        if int(price * 1.08) == N:
            print(price)
            return 
    
    print(":(")
    return

main()
```
</details>

## 5. Can you solve this? 

https://atcoder.jp/contests/abc121/tasks/abc121_b

<details><summary>ポイント</summary>

書いてあることに忠実に実装すると`AC`。

</details>
<br>

所要時間: 3分07秒

<details><summary>解答コード</summary>

```python
def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        a = list(map(int, input().split()))
        score = C
        for i in range(M):
            score += a[i]*B[i]
        if score > 0:
            ans += 1
    
    print(ans)

main()
```
</details>


## 6. Bishop 

https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b

<details><summary>ポイント</summary>

`H==1`や`W==1`のコーナーケースに注意。

</details>

所要時間: 7分10秒

<details><summary>解答コード</summary>

```python
def main():
    H, W = map(int, input().split())
    if H==1 or W==1:
        return 1
    ans = 0
    # odd * odd 
    if H%2 and W%2:
        ans = (H//2+1)*(W//2+1) + (H//2)*(W//2)
    # even * odd
    elif not H%2 and W%2:
        ans = (H//2)*(W//2+1) + (H//2)*(W//2)
    # odd * even
    elif H%2 and not W%2:
        ans = (H//2+1)*(W//2) + (H//2)*(W//2)
    # even * even
    else:
        ans = (H//2)*W
    return ans 

print(main())
```
</details>


## 7. Bingo 

https://atcoder.jp/contests/abc157/tasks/abc157_b

<details><summary>ポイント</summary>

ビンゴになったかどうかを確認するための関数を用意しておくと便利。
二次元配列の平坦化には`itertools`の`chain.from_iterable`が使える。

参考文献

https://note.nkmk.me/python-list-flatten/

</details>
<br>

所要時間: 11分

<details><summary>解答コード</summary>

```python
from itertools import chain

def check(li: list) -> bool:

    for row in range(3):
        flag = True 
        for col in range(3):
            if not li[row][col]:
                flag = False 
        if flag: return flag 

    for col in range(3):
        flag = True 
        for row in range(3):
            if not li[row][col]:
                flag = False
        if flag: return flag
    
    if li[0][0] and li[1][1] and li[2][2]:
        return True 
    if li[0][2] and li[1][1] and li[2][0]:
        return True 
    
    return False 

def main():
    A = []
    for _ in range(3):
        a = list(map(int, input().split()))
        A.append(a)
    set_A = set(chain.from_iterable(A))
    N = int(input())
    turned = [[False, False, False] for _ in range(3)]
    for _ in range(N):
        b = int(input())
        if b in set_A:
            for row in range(3):
                for col in range(3):
                    if A[row][col] == b:
                        turned[row][col] = True
        else: continue 
    
    if check(turned):
        print("Yes")
    else:
        print("No")

main()
```
</details>


## 8. 1 21

https://atcoder.jp/contests/abc086/tasks/abc086_b

<details><summary>ポイント</summary>

最初から`str`型で取ると楽。

</details>
<br>

所要時間: 1分12秒

<details><summary>解答コード</summary>

```python
def main():
    a, b = map(str, input().split())
    num = int(a+b)
    if (num**0.5//1)**2 == num:
        print("Yes")
    else:
        print("No")

main()
```
</details>

## 9. Collecting Balls (Easy Version)

https://atcoder.jp/contests/abc074/tasks/abc074_b

所要時間: 2分12秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(x[i], abs(x[i]-K))*2
    print(ans)

main()
```
</details>

## 10. Card Game For Two

https://atcoder.jp/contests/abc088/tasks/abc088_b

所要時間: 3分7秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    Alice = 0
    Bob = 0
    
    for i in range(N):
        if not i%2: 
            Alice += A[i]
        else:
            Bob += A[i]
    
    print(Alice-Bob)

main()
```
</details>

## 11. Break Number 

https://atcoder.jp/contests/abc068/tasks/abc068_b

<details><summary>ポイント</summary>

二分探索。

</details>
<br>

所要時間：3分51秒

<details><summary>解答コード</summary>

```python
from bisect import bisect_right 

multiple_of_two = [2**i for i in range(8)]

def main():
    N = int(input())
    idx = bisect_right(multiple_of_two, N)
    print(multiple_of_two[idx-1])

main()
```
</details>


## 12. Travelling Salesman Around Lake 

https://atcoder.jp/contests/abc160/tasks/abc160_c

<details><summary>ポイント</summary>

円を繋げる。

</details>
<br>

所要時間: 4分14秒

<details><summary>解答コード</summary>

```python
def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    dist = []
    for i in range(N):
        if i == 0:
            dist.append(A[i]+(K-A[-1]))
        else:
            dist.append(A[i]-A[i-1])
    print(K-max(dist))

main()
```
</details>

## 13. Cookie Exchanges 

https://atcoder.jp/contests/agc014/tasks/agc014_a


所要時間: 5分13秒

<details><summary>解答コード</summary>

```python
def main():
    A, B, C = map(int, input().split())
    for i in range(10**6):
        if not A%2 and not B%2 and not C%2:
            A, B, C = B//2+C//2, A//2+C//2, A//2+B//2
        else:
            return i
    return -1

print(main())
```
</details>

## 14. Replacing Integers 

https://atcoder.jp/contests/abc161/tasks/abc161_c

所要時間: 2分46秒

<details><summary>解答コード</summary>

```python
def main():
    N, K = map(int, input().split())
    if N%K==0:
        return 0
    else:
        return min(abs(N%K-K), N%K)

print(main())
```
</details>

## 15. Divide Problems 

https://atcoder.jp/contests/abc132/tasks/abc132_c

所要時間：3分19秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    d = sorted(list(map(int, input().split())))

    left_bound = d[N//2-1]
    right_bound = d[N//2]

    print(right_bound-left_bound)

main()
```
</details>

## 16. Go To School 

https://atcoder.jp/contests/abc142/tasks/abc142_c

<details><summary>ポイント</summary>

添え字に注意。

</details>
<br>

所要時間：1分47秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0 for _ in range(N)]
    for i in range(N):
        ans[A[i]-1] = i+1
    print(*ans)

main()
```
</details>

## 17. Alchemist 

https://atcoder.jp/contests/abc138/tasks/abc138_c

<details><summary>ポイント</summary>

`float`型で。

</details>

所要時間：2分5秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    V = sorted(list(map(int, input().split())))
    ans = V[0]
    for i in range(1, N):
        ans = (ans+V[i])/2
    print(ans)

main()
```
</details>

## ATCoder 

https://atcoder.jp/contests/abc122/tasks/abc122_b

所要時間：４分

<details><summary>解答コード</summary>

```python

def main():
    target = set(["A", "C", "G", "T"])
    ans = 0
    S = list(input())
    for i in range(len(S)):
        if S[i] in target:
            length = 0
            for j in range(i, len(S)):
                if S[j] in target:
                    length += 1
                else:
                    break
            ans = max(ans, length)

    
    print(ans)

main()
            
```
</details>

## 19. Toll Games 

https://atcoder.jp/contests/abc094/tasks/abc094_b

<details><summary>ポイント</summary>

`0`地点でもゴールになることに注意。

</details>
<br>

所要時間：4分13秒

<details><summary>解答コード</summary>

```python
from bisect import bisect_right 

def main():
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    idx = bisect_right(A, X)
    print(min(M-idx, idx))

main()
```
</details>

## 20. Collatz Problem 

https://atcoder.jp/contests/abc116/tasks/abc116_b

<details><summary>ポイント</summary>

`x in set`の判定は`O(1)`。

</details>
<br>

所要時間：3分24秒

<details><summary>解答コード</summary>

```python
def main():
    s = int(input())
    numbers = set()
    numbers.add(s)
    cnt = 1
    n = s
    while True:

        if n%2: n=3*n+1
        else: n//=2
        cnt += 1
        if n in numbers:
            break 
        else:
            numbers.add(n)
    
    print(cnt)

main()
```
</details>

## 21. Next Prime 

https://atcoder.jp/contests/abc149/tasks/abc149_c

<details><summary>ポイント</summary>

`O(\sqrt{n})`の素数判定法がアルゴ式にある。

参考文献

https://algo-method.com/descriptions/93

</details>
<br>

所要時間：1分43秒

<details><summary>解答コード</summary>

```python
from math import sqrt, ceil

def isprime(N):
    flag = True
    if N == 1: return False
    if N == 2: return True
    
    for i in range(ceil(sqrt(N))+1):
        if i <= 1: continue
        elif N%i == 0: 
            flag = False
    return flag 

def main():
    X = int(input())
    ans = X
    while True:
        if isprime(ans):
            break 
        else:
            ans += 1
    print(ans)

main()
```
</details>

## 22. Candy Distribution Again 

https://atcoder.jp/contests/agc027/tasks/agc027_a

<details><summary>ポイント</summary>

場合分け。

</details>
<br>

所要時間：5分57秒

<details><summary>解答コード</summary>

```python
def main():
    N, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    ans = 0

    if x > sum(a):
        return N-1

    for i in range(N):
        if x >= a[i]:
            x -= a[i]
            ans += 1
        else:
            break 
    
    return ans

print(main())
```
</details>

## 23. Chocolate 

https://atcoder.jp/contests/abc092/tasks/abc092_b

所要時間」：1分59秒

<details><summary>解答コード</summary>

```python
from math import ceil
def main():
    N = int(input())
    D, X = map(int, input().split())
    ans = X
    for _ in range(N):
        a = int(input())
        ans += ceil(D/a)
    
    print(ans)

main()
```
</details>

## 24. Nice Shopping 

https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_b

所要時間：3分36秒

<details><summary>解答コード</summary>

```python
def main():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    price = min(a) + min(b)
    for _ in range(M):
        x,y,c = map(int, input().split())
        price = min(price, a[x-1]+b[y-1]-c)
    print(price)

main()
```
</details>

## 25. Count Order 

https://atcoder.jp/contests/abc150/tasks/abc150_c

<details><summary>ポイント</summary>

解説にもあるが`8!`は`40320`なので全探索しても間に合う。

https://blog.hamayanhamayan.com/entry/2020/01/11/144924


</details>
<br>

所要時間：4分20秒

<details><summary>解答コード</summary>

```python
from itertools import permutations 
from bisect import bisect_right

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    N_perm = sorted(permutations(P))
    P_idx = bisect_right(N_perm, tuple(P))
    Q_idx = bisect_right(N_perm, tuple(Q))
    print(abs(P_idx-Q_idx))

main()
```
</details>


## 26. Caracal vs Monster 

https://atcoder.jp/contests/abc153/tasks/abc153_d

<details><summary>ポイント</summary>

モンスターの個体も管理しておいて一気に片を付ける。同じ操作でモンスターの数は2倍。

</details>
<br>

所要時間：2分31秒

<details><summary>解答コード</summary>

```python
def main():
    H = int(input())
    cnt = 0
    num = 1
    while True:
        if H==1:
            cnt += 1
            break 
        H //= 2
        num *= 2
        cnt += num
    print(cnt)

main()
```
</details>

## 27. Count Balls 

https://atcoder.jp/contests/abc158/tasks/abc158_b

所要時間：2分25秒

<details><summary>解答コード</summary>

```python
def main():
    N, A, B = map(int, input().split())
    ans = (N // (A+B)) * A
    ans += min(N%(A+B), A)
    print(ans)
main()
```
</details>

## 28. Shift Only 

https://atcoder.jp/contests/abc081/tasks/abc081_b

所要時間：3分49秒

<details><summary>解答コード</summary>

```python

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**18
    for i in range(N):
        num = A[i]
        cnt = 0
        while True:
            if num%2:
                break 
            num //= 2
            cnt += 1
        ans = min(ans, cnt)
    print(ans)
main()

```
</details>

## 29. 754 

https://atcoder.jp/contests/abc114/tasks/abc114_b


所要時間：1分45秒

<details><summary>解答コード</summary>

```python
def main():
    S = list(input())
    diff = 753
    for i in range(len(S)-2):
        num = S[i] + S[i+1] + S[i+2]
        diff = min(diff, abs(753-int(num)))
    print(diff)

main()
```
</details>

## 30. Ruined Square 

https://atcoder.jp/contests/abc108/tasks/abc108_b

<details><summary>ポイント</summary>

回転行列を知っていると解きやすいらしい。

https://blog.hamayanhamayan.com/entry/2018/09/02/223200

私はお絵かきをしながら色々考えて解答。

</details>
<br>

所要時間：14分49秒

<details><summary>解答コード</summary>

```python
def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2+y1-y2 
    y3 = y2-x1+x2
    x4 = x1+y1-y2
    y4 = y1-x1+x2
    print(x3, y3, x4, y4)

main()
```

</details>

