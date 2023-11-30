
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

## 18. ATCoder 

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

## 31. Varied 

https://atcoder.jp/contests/abc063/tasks/abc063_b

所要時間：1分16秒

<details><summary>解答コード</summary>

```python
def main():
    S =list(input())
    S_set = set(S)
    if len(S) == len(S_set):
        print("yes")
    else:
        print("no")
    
main()
```

</details>


## 32. Increment Decrement 

https://atcoder.jp/contests/abc052/tasks/abc052_b

所要時間：1分53秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    S = list(input())
    x = 0
    max_x = 0
    for i in range(N):
        if S[i] == "I":
            x+=1
        else:
            x-=1
        max_x = max(max_x, x)
    
    print(max_x)

main()
```

</details>

## 33. Postal Code

https://atcoder.jp/contests/abc084/tasks/abc084_b

所要時間：3分6秒

<details><summary>解答コード</summary>

```
def main():
    A, B = map(int, input().split())
    S = list(input())
    ans = True
    for i in range(len(S)):
        if i == A:
            if S[i] != "-":
                ans = False 
            else:
                continue 
        else:
            if S[i].isdigit():
                continue
            else:
                ans = False
    
    if ans:
        print("Yes")
    else:
        print("No")

main()
```
</details>


## 34. Coins 

https://atcoder.jp/contests/abc087/tasks/abc087_b

所要時間：2分

<details><summary>解答コード</summary>

```python
def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    cnt = 0

    for five_hundred in range(A+1):
        for hundred in range(B+1):
            for fifty in range(C+1):
                if five_hundred*500+hundred*100+fifty*50==X:
                    cnt += 1
    
    print(cnt)

main()
```

</details>

## 35. Not Found 

https://atcoder.jp/contests/abc071/tasks/abc071_b


<details><summary>ポイント</summary>

アルファベット小文字のリストを持っておく。

```python
lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

</details>
<br>

所要時間：5分41秒

<details><summary>解答コード</summary>

```python
lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    S = set(list(input()))
    lowercase_list_bool = [(False) for _ in range(26)]
    for i in range(26):
        if lowercase_list[i] in S:
            lowercase_list_bool[i] = True
    ans = None
    for j in range(26):
        if not lowercase_list_bool[j]: 
            ans = lowercase_list[j]
            return ans
    
    return ans 

print(main())
```

</details>


## 36 Prison 

https://atcoder.jp/contests/abc127/tasks/abc127_c

所要時間：6分23秒

<details><summary>解答コード</summary>

```python
def main():
    N, M = map(int, input().split())
    max_l = 0
    min_r = 10**18
    for _ in range(M):
        l, r = map(int, input().split())
        max_l = max(max_l, l)
        min_r = min(min_r, r)

    if max_l > min_r:
        print(0)
    else:
        print(min_r-max_l+1)

main()
```

</details>

## 37. Attack Survival 

https://atcoder.jp/contests/abc141/tasks/abc141_c

<details><summary>ポイント</summary>

全員から1点引くのではなく正答者に1点を与える。

</details>
<br>

所要時間：7分6秒

<details><summary>解答コード</summary>

```python
def main():
    N, K, Q = map(int, input().split())
    players_point = [(K) for _ in range(N)]
    for _ in range(Q):
        a = int(input())
        players_point[a-1] += 1
    
    for player in range(N):
        if players_point[player] <= Q:
            print("No")
        else:
            print("Yes")
    
main()
```

</details>



## 38. Five Dishes 

https://atcoder.jp/contests/abc123/tasks/abc123_b

所要時間：10分25秒

<details><summary>解答コード</summary>

```python
from math import ceil
def main():
    dish_list = []
    for _ in range(5):
        dish_list.append(int(input()))

    mod_last_dish = min([(i-1)%10 for i in dish_list])

    cnt = 0
    had_last_meal = False

    for i in range(5):
        if (dish_list[i]-1)%10 == mod_last_dish and not had_last_meal:
            cnt += dish_list[i]
            had_last_meal = True
        else:
            cnt += ceil(dish_list[i]/10)*10
    
    print(cnt)

main()
```

</details>

## 39. Exception Handling 

https://atcoder.jp/contests/abc134/tasks/abc134_c

所要時間：4分6秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        A.append(a)
    A_sorted = sorted(A, reverse = True)
    for item in range(N):
        if A[item] == A_sorted[0]:
            print(A_sorted[1])
        else:
            print(A_sorted[0])

main()
```

</details>


## 40. Range Product 

https://atcoder.jp/contests/agc002/tasks/agc002_a

所要時間：2分59秒

<details><summary>解答コード</summary>

```python
def main():
    a, b = map(int, input().split())
    if a <= 0 <= b:
        print("Zero")
    elif a < 0:
        cnt = 0
        if b > 0:
            cnt = abs(a)
        else:
            cnt = abs(a-b)+1
        if cnt%2:
            print("Negative")
        else:
            print("Positive")
    else:
        print("Positive")

main()
```

</details>


## 41. Low Elements 

https://atcoder.jp/contests/abc152/tasks/abc152_c

所要時間：5分8秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_p = P[0]
    cnt = 0
    for i in range(N):
        if P[i] <= min_p:
            cnt += 1
            min_p = P[i]
    
    print(cnt)

main()
```

</details>

## 42. Foods Loved by Everyone 

https://atcoder.jp/contests/abc118/tasks/abc118_b

所要時間：3分35秒

<details><summary>解答コード</summary>

```python
def main():
    N, M = map(int, input().split())
    foods_list = [(0) for _ in range(M+1)]
    for _ in range(N):
        a = list(map(int, input().split()))
        for item in range(1, len(a)):
            foods_list[a[item]] += 1
    cnt = 0
    for food in range(M+1):
        if foods_list[food] == N:
            cnt += 1
    
    print(cnt)

main()
```

</details>

## 43. Beautiful Strings

https://atcoder.jp/contests/abc044/tasks/abc044_b

<details><summary>ポイント</summary>

Pythonでは`collections`の`Counter`クラスが使える。

https://note.nkmk.me/python-collections-counter/

</details>
<br>

所要時間：3分19秒

<details><summary>解答コード</summary>

```python
from collections import Counter
def main():
    w = list(input())
    c = Counter(w)
    ans = True
    for item in c.values():
        if item%2:
            ans = False
    
    if ans:
        print("Yes")
    else:
        print("No")

main()
```

</details>


## 44. Coloring Colorfully 

https://atcoder.jp/contests/abc124/tasks/abc124_c

所要時間：4分1秒

<details><summary>解答コード</summary>

```python
def main():
    S = [int(i) for i in list(input())]
    odd = []
    even = []
    for idx in range(len(S)):
        if idx%2:
            odd.append(S[idx])
        else:
            even.append(S[idx])
    
    # if all even are to be black 
    even_black = sum(even) + (len(odd)-sum(odd))
    # if all odd are to be black
    odd_black = sum(odd) + (len(even)-sum(even))

    print(min(even_black, odd_black))

main()
```

</details>

## 45. Palindromic Numbers 

https://atcoder.jp/contests/abc090/tasks/abc090_b

所要時間：3分20秒

<details><summary>解答コード</summary>

```python
def main():
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        sentence = list(str(i))
        if sentence == sentence[::-1]:
            cnt += 1
    print(cnt)

main()
```

</details>


## 46. Fairness 

https://atcoder.jp/contests/agc024/tasks/agc024_a

所要時間：4分35秒

<details><summary>解答コード</summary>

```python
def main():
    A, B, C, K = map(int, input().split())
    if K%2:
        return (A-B)*(-1)
    else:
        return A-B

print(main())
```

</details>

## 47. Lucas Number 

https://atcoder.jp/contests/abc079/tasks/abc079_b

所要時間：4分53秒

<details><summary>解答コード</summary>

```python
def check_lucas_number(n: int) -> int:    
    lucas_number = [(0) for _ in range(87)]
    for i in range(87):
        if i == 0: 
            lucas_number[i] = 2
        elif i == 1:
            lucas_number[i] = 1
        else:
            lucas_number[i] = lucas_number[i-2]+lucas_number[i-1]
    
    return lucas_number[n]

def main():
    N = int(input())
    print(check_lucas_number(N))

main()
```

</details>


## 48. Lower 

https://atcoder.jp/contests/abc139/tasks/abc139_c

<details><summary>ポイント</summary>

`N=1`のコーナーケースに注意。

</details>
<br>

所要時間：7分53秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans_length = []

    # Corner Case 
    if N == 1:
        return 0

    cnt = 0
    left = 0
    right = 1
    while True:
        if H[left] >= H[right]:
            cnt += 1
            left += 1
            right += 1
        else:
            ans_length.append(cnt)
            cnt = 0
            left +=1
            right += 1
        
        if right == N:
            ans_length.append(cnt)
            break 
    
    return max(ans_length)


print(main())
```

</details>


## 49. Picture Frame 

https://atcoder.jp/contests/abc062/tasks/abc062_b

<details><summary>ポイント</summary>

`list`型の前に`#`を挿入するのは`insert()`メソッドで可能だが、リスト内全要素をずらす（`O(N)`）ので制約には注意が必要。

https://note.nkmk.me/python-list-append-extend-insert/#insert

計算量を削減したい場合は`collections`モジュールの`deque`クラスから`appendleft()`が`O(1)`で使える。

https://note.nkmk.me/python-collections-deque/

文字列の結合には`join()`を使う。

https://hibiki-press.tech/python/join/582

</details>
<br>

所要時間：3分35秒

<details><summary>解答コード</summary>

```python
def main():
    H, W = map(int, input().split())
    ans = []
    ans.append("#" for _ in range(W+2))
    for _ in range(H):
        a = list(input())
        a.insert(0, "#")
        a.append("#")
        ans.append(a)
    ans.append("#" for _ in range(W+2))

    for i in range(len(ans)):
        to_print = "".join(ans[i])
        print(to_print)

main()
```

</details>

## 50. Comparison 

https://atcoder.jp/contests/abc059/tasks/abc059_b


<details><summary>ポイント</summary>

Pythonは多倍長整数に対応しているのでこういう問題は楽。

https://qiita.com/square1001/items/1aa12e04934b6e749962#2-1-%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%A7%E3%82%82%E5%A4%A7%E3%81%8D%E3%81%AA%E6%95%B0%E3%82%92%E6%89%B1%E3%81%84%E3%81%9F%E3%81%84

</details>

所要時間：46秒

<details><summary>解答コード</summary>

```python
def main():
    A = int(input())
    B = int(input())
    if A > B:
        print("GREATER")
    elif A < B:
        print("LESS")
    else:
        print("EQUAL")

main()
```

</details>

## 51. Some Sums 

https://atcoder.jp/contests/abc083/tasks/abc083_b

所要時間：2分5秒

<details><summary>解答コード</summary>

```python
def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        str_num = str(i)
        str_num_sum = sum([int(z) for z in list(str_num)])
        if A <= str_num_sum <= B:
            ans += i
    
    print(ans)

main()
```

</details>

## 52. Maximal Value 

https://atcoder.jp/contests/abc140/tasks/abc140_c

所要時間：5分46秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    B = list(map(int, input().split()))
    A = [(0) for _ in range(N)]
    for i in range(N):
        if i == 0:
            A[i] = B[0]
        elif i == N-1:
            A[i] = B[-1]
        else:
            A[i] = min(B[i], B[i-1])
    
    print(sum(A))

main()
```

</details>

## 53. Counting Roads 

https://atcoder.jp/contests/abc061/tasks/abc061_b

所要時間：2分10秒

<details><summary>解答コード</summary>

```python
def main():
    N, M = map(int, input().split())
    roads = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        roads[a-1].append(b-1)
        roads[b-1].append(a-1)
    for city in range(N):
        print(len(roads[city]))

main()
```

</details>

## 54. Shiritori 

https://atcoder.jp/contests/abc109/tasks/abc109_b

所要時間：4分16秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    last_letter = 0
    said_word = set()
    for i in range(N):
        w = str(input())
        if i == 0:
            last_letter = w[-1]
            said_word.add(w)
        else:
            if last_letter == w[0] and w not in said_word:
                last_letter = w[-1]
                said_word.add(w)
                continue 
            else:
                return False
    
    return True 

if main():
    print("Yes")
else:
    print("No")
```

</details>

## 55. Good Distance 

https://atcoder.jp/contests/abc133/tasks/abc133_b

所要時間：5分49秒

<details><summary>解答コード</summary>

```python
squared_number_set = set([n*n for n in range(1000)])

def main():
    N, D = map(int, input().split())
    points = []
    for _ in range(N):
        x = list(map(int, input().split()))
        points.append(x)
    
    cnt = 0
    for y in range(N):
        for z in range(y+1, N):
            distance = 0
            for d in range(D):
                distance += (points[y][d] - points[z][d])**2
            if distance in squared_number_set:
                cnt += 1
    
    print(cnt)

main()
```
</details>

## 56. Small and Large Integers 

https://atcoder.jp/contests/abc093/tasks/abc093_b

所要時間：1分59秒

<details><summary>解答コード</summary>

```python
def main():
    A, B, K = map(int, input().split())
    for i in range(A, B+1):
        if i <= A+K-1:
            print(i)
        elif i >= B-K+1:
            print(i)

main()
```

</details>

## 57. Tax Increase 

https://atcoder.jp/contests/abc158/tasks/abc158_c

所要時間：5分50秒

<details><summary>解答コード</summary>

```python
def original_price(price :int, tax: int) -> list:
    p = int(price // (tax/100))
    price_list = []
    for possible_price in range(p-100, p+100):
        if possible_price * tax // 100 == price:
            price_list.append(possible_price)
    return price_list

def main():
    A, B = map(int, input().split())
    A_list= original_price(A, 8)
    B_list = original_price(B, 10)
    for price in A_list:
        if price in set(B_list):
            return price 
    
    return "-1"

print(main())
```

</details>

## 58. Palace 

https://atcoder.jp/contests/abc113/tasks/abc113_b

所要時間：8分4秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H_temp = [T-x*0.006 for x in H]
    diff = -10**18
    idx = 0
    for i in range(N):
        if abs(H_temp[i]-A) < abs(diff-A):
            diff = H_temp[i]
            idx = i
    print(idx+1)

main()
```

</details>

## 59. AcCepted 

https://atcoder.jp/contests/abc104/tasks/abc104_b

所要時間：5分32秒

<details><summary>解答コード</summary>

```python

def main():
def main():
    S = list(input())
    
    # first letter being "A"
    if S[0] != "A":
        return False 
    

    # having one "C"
    if S[2:-1].count("C") != 1:
        return False 
    
    for i in range(1, len(S)):
        if S[i] == "C" and 2 <= i <= len(S)-2:
            continue 
        elif S[i].islower():
            continue
        else:
            return False
    
    return True 

if main():
    print("AC")
else:
    print("WA")

```

</details>


## 60. Contest with Drinks Easy 


https://atcoder.jp/contests/abc050/tasks/abc050_b

所要時間：3分30秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    save = 10**18
    for _ in range(M):
        p, x = map(int, input().split())
        print(sum(T)-(T[p-1]-x))

main()
```

</details>


## 61. String Rotation 

https://atcoder.jp/contests/abc103/tasks/abc103_b


所要時間：3分2秒

<details><summary>解答コード</summary>

```python
def main():
    S = list(input())
    T = list(input()) * 2

    ans = False
    for i in range(len(S)):
        if T[i:i+len(S)] == S:
            ans = True
    
    if ans:
        print("Yes")
    else:
        print("No")

main()
```

</details>


## 62. Thin

https://atcoder.jp/contests/abc049/tasks/abc049_b

所要時間：1分36秒

<details><summary>解答コード</summary>

```python
def main():
    H, W = map(int, input().split())
    for _ in range(H):
        c=input()
        print(c)
        print(c)

main()
```

</details>

## 63. Brick Break 

https://atcoder.jp/contests/abc148/tasks/abc148_d

所要時間：3分8秒

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    a = list(map(int, input().split()))
    idx = 1
    cnt = 0
    for i in range(N):
        if a[i] == idx:
            cnt += 1
            idx += 1
    
    if cnt == 0:
        print(-1)
    else:
        print(N-cnt)
main()
```

</details>

## 64. ∵∴∵

https://atcoder.jp/contests/abc058/tasks/abc058_b

所要時間：4分18秒

<details><summary>解答コード</summary>

```python
def main():
    O = list(input())
    E = list(input())
    ans = ""
    for i in range(len(O)+len(E)):
        if i%2: 
            ans += E[i//2]
        else:
            ans += O[i//2]
    print(ans)

main()
```

</details>

## 65. A to Z String

https://atcoder.jp/contests/abc053/tasks/abc053_b

<details><summary>解答コード</summary>

```python
def main():
    s = list(input())
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i] == "A":
            start = i
            break 
    for j in reversed(range(len(s))):
        if s[j] == "Z":
            end = j
            break 
    print(end-start+1)

main()
```

</details>


## 66. Wanna go back home 

https://atcoder.jp/contests/agc003/tasks/agc003_a

所要時間：3分26秒

<details><summary>解答コード</summary>

```python
def main():
    S = list(input())
    north = S.count("N")
    south = S.count("S")
    east = S.count("E")
    west = S.count("W")

    if not ((north>0 and south>0) or (north == south == 0)):
        print("No")
        return 
    
    if not ((west>0 and east>0) or (west==east==0)):
        print("No")
        return
    
    print("Yes")
    return 

main()
```

</details>

## 67. Poll

https://atcoder.jp/contests/abc155/tasks/abc155_c

<details><summary>ポイント</summary>

`collections`モジュールの`Counter`クラスには`most_common()`という要素と出現回数をソートして返してくれるメソッドが。

https://qiita.com/ell/items/259388b511e24625c0d7

</details>
<br>

所要時間：6分31秒

<details><summary>解答コード</summary>

```python
from collections import Counter
def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    
    S_counted = Counter(S)
    S_counted_sorted = S_counted.most_common()

    max_num = S_counted_sorted[0][1]
    ans = sorted([i[0] for i in S_counted.items() if i[1] == max_num])

    for i in ans:
        print(i)

main()
```

</details>

## 68. Guidebook 

https://atcoder.jp/contests/abc128/tasks/abc128_b

<details><summary>ポイント</summary>

多次元リストでの用いてのソートは`operator`の`itemgetter`が便利。

https://qiita.com/t_kanno/items/13dd226e70d080159d97

</details>

所要時間：9分40秒

<details><summary>ポイント</summary>

```python
from operator import itemgetter 

def main():
    N = int(input())
    restaurant = []
    for i in range(N):
        s, p = map(str, input().split())
        restaurant.append([i+1, s, int(p)])
    
    sorted_by_point = sorted(restaurant, key=itemgetter(2), reverse=True)
    sorted_by_name = sorted(sorted_by_point, key=itemgetter(1))

    for j in range(N):
        print(sorted_by_name[j][0])
main()
```


</details>

## 69. Dividing a String 

https://atcoder.jp/contests/agc037/tasks/agc037_a

<details><summary>ポイント</summary>

DPか工夫した貪欲で解けるらしい。1つだけ難易度違いすぎない？

https://drken1215.hatenablog.com/entry/2020/11/11/164900

https://betrue12.hateblo.jp/entry/2020/05/01/201510

</details>

<br>

<details><summary>コード</summary>

:::note warn
追記
貪欲で書いたが嘘解法っぽいのでまた検討する。
:::

```python

def main():
    S = input()

    cnt = 0
    curr = ""
    prev = ""

    for i in range(len(S)):
        curr += S[i]
        if prev != curr:
            cnt += 1
            prev = curr
            curr = ""
    print(cnt)

main()
```

</details>


## 70. 100 to 105

https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c

<details><summary>解答コード</summary>

```python
def main():
    X = int(input())

    dp = [(0) for _ in range(X+1)]
    dp[0] = 1

    for i in range(X+1):
        if dp[i]:
            for j in range(100, 106):
                if i+j <= X:
                    dp[i+j] = 1
    
    print(dp[X])

main()
```

</details>

