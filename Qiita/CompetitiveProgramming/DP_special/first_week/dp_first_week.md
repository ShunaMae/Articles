# 初めに

こんにちは、Pittaです。先週はDPを勉強しようと思って問題を解いていたので、それの共有をしようと思います。

競プロで基本的なアルゴリズムを勉強しようと思ったら、やはり[アルゴ式](https://algo-method.com)が一番だと思います。易しい問題から少しづつ発展していくので、ゼロから学ぶのに最適です。

競プロ本なども良いのですが、やはり問題数と解説の充実度でアルゴ式が一番お気に入りです。

# アルゴ式　動的計画法

## 動的計画法（１）イントロダクション

このセクションで動的計画法と何でどうすれば解けるのかがつかめました。

### Q1. 数字の列

<details><summary>解答コード</summary>

```python
def main():
    N, X, Y = map(int, input().split())
    a = [X, Y]
    for i in range(2, N):
        a.append((a[i-1] + a[i-2]) % 100)
    
    print(a[N-1])
    return 

main()
```

</details>

### Q2. マスの移動（１）

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [(10**18) for _ in range(N)]
    dp[0] = 0
    dp[1] = A[0]

    for grid in range(1, N):
        dp[grid] = min(dp[grid-1]+A[grid], dp[grid-2]+2*A[grid])
    
    print(dp[-1])

main()
```

</details>


### Q3. 階段ののぼり方

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    dp = [(0) for _ in range(N+1)]
    dp[0] = 1

    for i in range(1, N+1):
        dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
    
    print(dp[N])

main()

```

</details>


### Q4. タイルの敷き詰め

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    dp = [(0) for _ in range(N)]
    dp[0] = 1

    for i in range(1, len(dp)):
        if i == 1:
            dp[i] += 1
        if i == 2:
            dp[i] += 1
        dp[i] += dp[i-1]
        if i-2 >= 0:
            dp[i] += dp[i-2]
        if i-3 >= 0:
            dp[i] += dp[i-3]

    print(dp[N-1])

main()

```

</details>


### Q5. マスの移動（2）

<details><summary>解答コード</summary>

```python

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [(10**18) for _ in range(N)]
    dp[0] = 0
    
    for i in range(1, len(dp)):
        for j in range(1, M+1):
            if i-j >= 0:
                dp[i] = min(dp[i], dp[i-j]+j*A[i])
    
    print(dp[-1])

main()

```

</details>

### Q6. すごろく

<details><summary>解答コード</summary>

```python
def main():
    N, M = map(int, input().split())
    D = list(map(int, input().split()))

    dp = [(False) for _ in range(N+1)]
    dp[0] = True 

    for i in range(N):
        for j in range(M):
            if i + D[j] <= N and dp[i]:
                dp[i+D[j]] = True
    
    return dp[-1]

if main():
    print("Yes")
else:
    print("No")

```


</details>



## 動的計画法（２）2次元の動的計画法

ナップサック問題の前提知識となる２次元動的計画法がしっかりと学べます。


### Q1. 表と数字（１）

<details><summary>解答コード</summary>

```python

def main():
    a = list(map(int, input().split()))
    dp = [[(0) for _ in range(4)] for _ in range(4)]
    dp[0] = a

    for row in range(1, len(dp)):
        for col in range(4):
            dp[row][col] += dp[row-1][col]
            if col-1 >= 0:
                dp[row][col] += dp[row-1][col-1]
            if col + 1 <= 3:
                dp[row][col] += dp[row-1][col+1]
    
    print(dp[-1][-1])

main()
            

```


</details>

### Q2. 表と数字（２）


<details><summary>解答コード</summary>

```python

def main():
    N = int(input())
    a = list(map(int, input().split()))
    dp = [[(0) for _ in range(N)] for _ in range(N)]
    dp[0] = a

    for row in range(1, len(dp)):
        for col in range(N):
            dp[row][col] += dp[row-1][col]
            if col-1 >= 0:
                dp[row][col] += dp[row-1][col-1]
            if col + 1 < N:
                dp[row][col] += dp[row-1][col+1]
            dp[row][col] %= 100
    
    print(dp[-1][-1])

main()
            

```

</details>


### Q3. 3つの仕事


<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    dp = [[(0) for _ in range(3)] for _ in range(N)]
    dp[0] = A[0]
    for day in range(1, N):
        dp[day][0] = max(dp[day-1][1], dp[day-1][2]) + A[day][0]
        dp[day][1] = max(dp[day-1][0], dp[day-1][2]) + A[day][1]
        dp[day][2] = max(dp[day-1][0], dp[day-1][1]) + A[day][2]
    
    print(max(dp[-1]))

main()
```

</details>


### Q4. コマの移動（１）

<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    dp = [[(0) for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for row in range(N):
        for col in range(N):
            if col-1 >= 0:
                dp[row][col] += dp[row][col-1]
            if row-1 >= 0:
                dp[row][col] += dp[row-1][col]
    
    print(dp[-1][-1])

main()
```

</details>

### Q5. コマの移動（２）


<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(input()))
    dp = [[(0) for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for row in range(N):
        for col in range(N):
            if col-1 >= 0 and S[row][col] == ".":
                dp[row][col] += dp[row][col-1]
            if row-1 >= 0 and S[row][col] == ".":
                dp[row][col] += dp[row-1][col]
    
    print(dp[-1][-1])

main()
```

</details>


### Q6. コマの移動（３）


<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))
    dp = [[(0) for _ in range(N)] for _ in range(N)]
    dp[0][0] = S[0][0]

    for row in range(N):
        for col in range(N):
            if col-1 >= 0:
                dp[row][col] = max(dp[row][col], dp[row][col-1] + S[row][col])
            if row-1 >= 0:
                dp[row][col] = max(dp[row][col], dp[row-1][col] + S[row][col])
    
    print(dp[-1][-1])

main()
```

</details>


### Q7. コマの移動（４）


<details><summary>解答コード</summary>

```python
def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split()))[::-1])
    dp = [[(10**18) for _ in range(N)] for _ in range(N)]
    dp[0][0] = S[0][0]

    for row in range(N):
        for col in range(N):
            if col-1 >= 0:
                dp[row][col] = min(dp[row][col], dp[row][col-1] + S[row][col])
            if row-1 >= 0:
                dp[row][col] = min(dp[row][col], dp[row-1][col] + S[row][col])
    
    print(dp[-1][-1])

main()
```

</details>


## 動的計画法（３）ナップサック問題

### Q1. 部分和問題（導入）



