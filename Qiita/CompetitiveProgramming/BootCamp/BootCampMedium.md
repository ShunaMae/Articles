
## 001. Trained?

https://atcoder.jp/contests/abc065/tasks/abc065_b

<details><summary>ポイント</summary>

グラフ問題に見えるが配列を順番に追っていけば解ける。

</details>


<details><summary>コード</summary>

```python
def main():
    N = int(input())
    Light = []

    # [Light, idx]
    for i in range(N):
        a = int(input())
        Light.append([a-1, i])
    
    cur_idx = 0
    cur_light = Light[0][0]
    cnt = 0
    
    while True:

        if cur_idx == 1:
            break
        if cnt > N:
            break

        cur_idx = Light[cur_light][1]
        cur_light = Light[cur_light][0]
        cnt += 1
    
    if cnt > N:
        print(-1)
    else:
        print(cnt)
        
main()

```

</details>

## 002. Irreevrsible Operation 

https://atcoder.jp/contests/agc029/tasks/agc029_a

<details><summary>ポイント</summary>

何回か実験をしてみると全てのBが右に来るまで操作が続くことがわかるので、そうなるまでの操作回数を（Bが全て右に来た時のインデックスの合計-現在のBのインデックスの合計）で計算する。

</details>


<details><summary>コード</summary>

```python
def my_ceil(N, W):
    return (-(-N//W))

def main():
    S = list(input())

    idx_cnt = 0
    for i in range(len(S)):
        if S[i] == "B":
            idx_cnt += i
    
    right_cnt = 0
    for j in range(S.count("B")):
        right_cnt += len(S)-j-1
    
    print(right_cnt-idx_cnt)

main()
```

</details>

## 003. >< 

https://atcoder.jp/contests/agc040/tasks/agc040_a

<details><summary>コード</summary>

```python
def main():
    S = input()

    more_than_count = [(0) for _ in range(len(S)+1)]
    less_than_count = [(0) for _ in range(len(S)+1)]

    for i in range(len(S)):
        if S[i] == "<":
            more_than_count[i+1] = more_than_count[i] + 1
    
    for j in reversed(range(len(S))):
        if S[j] == ">":
            less_than_count[j] = less_than_count[j+1] + 1
    
    ans = 0
    for k in range(len(S)+1):
        ans += max(more_than_count[k], less_than_count[k])
    
    print(ans)
    
main()
```

</details>


## 004. ss 

https://atcoder.jp/contests/abc066/tasks/abc066_b

<details><summary>コード</summary>

```python
def check_ss(s: list) -> bool:
    if len(s)%2:
        return False
    
    mid_point = len(s)//2
    if s[:mid_point] == s[mid_point:]:
        return True
    
    return False


def main():
    S = list(input())
    for _ in range(len(S)):
        S.pop()
        if check_ss(S):
            return len(S)

print(main())
    

```

</details>

## 005. ModSum

https://atcoder.jp/contests/abc139/tasks/abc139_d

<details><summary>ポイント</summary>

一回全探索するコードを書いて実験してみるとパターンが見えてくる。

```python:全探索コード

def greedy(n):
    from itertools import permutations 
    seq = list(range(1,n+1))
    perm_list = list(permutations(seq))
    
    ans = 0
    ans_seq = seq
    for s in perm_list:
        temp_ans = 0
        for i in range(len(s)):
            temp_ans += seq[i]%s[i]
        
        if temp_ans > ans:
            ans_seq = s
            ans = temp_ans
        else:
            continue
    
    print(ans)
    print(ans_seq)

```

</details>


<details><summary>コード</summary>

```python
def main():
    N = int(input())
    print((N)*(N-1)//2)

main()
```

</details>


## 006. Minesweeper 

https://atcoder.jp/contests/abc075/tasks/abc075_b

<details><summary>ポイント</summary>

上下左右斜めのマスをそれぞれ確認するときには`dir`のようなリストを使うと楽。

```python: 方向のリスト
dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
```

</details>

<details><summary>コード</summary>

```python

dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    grids = [[(0) for _ in range(W)] for _ in range(H)]


    for row in range(H):
        for col in range(W):
            if S[row][col] == "#":
                grids[row][col] = "#"
            
                for r, c in dir:
                    adj_row = row+r
                    adj_col = col+c
                    if (0 <= adj_row < H and \
                        0 <= adj_col < W and \
                            S[adj_row][adj_col] == "."):
                        
                        grids[adj_row][adj_col] += 1
    
    for i in grids:
        ans = "".join([str(z) for z in i])
        print(ans)


main()
```

</details>

## 007. Cut and Count 

https://atcoder.jp/contests/abc098/tasks/abc098_b

<details><summary>コード</summary>

```python
def main():
    N = int(input())
    S = list(input())

    ans = 0
    for i in range(1, N-1):
        first_set = set(S[:i])
        second_set = set(S[i:])
        cnt = 0
        for item in first_set:
            if item in second_set:
                cnt += 1
        
        ans = max(cnt, ans)
    
    print(ans)

main()
```

</details>

## 008. Colorful Leaderboard 

https://atcoder.jp/contests/abc064/tasks/abc064_c


<details><summary>コード</summary>

なんか楽しかったのでしっかり書いたが、解説にもあるようにレートをリストで持っておけばもっと簡単に書ける。なぜこの問題が茶中位diffなんだろう？


```python
def main():
    N = int(input())
    A = list(map(int, input().split()))

    top_coder = 0
    color_set = set()

    for i in range(N):
        if A[i] < 400:
            color_set.add("grey")
        elif A[i] < 800:
            color_set.add("brown")
        elif A[i] < 1200:
            color_set.add("green")
        elif A[i] < 1600:
            color_set.add("skyblue")
        elif A[i] < 2000:
            color_set.add("blue")
        elif A[i] < 2400:
            color_set.add("yellow")
        elif A[i] < 2800:
            color_set.add("orange")
        elif A[i] < 3200:
            color_set.add("red")
        else:
            top_coder += 1 
    
    max_num = len(color_set) + top_coder
    min_num = 1 if len(color_set) == 0 else len(color_set)

    print(min_num, max_num)

main()
```

</details>

## 009. Choose Integers 

https://atcoder.jp/contests/abc060/tasks/abc060_b 


<details><summary>ポイント</summary>

立式するとユークリッドの互除法を使う問題に帰着できる。
細かい解説は[こちら](https://qiita.com/drken/items/0c88a37eec520f82b788#%E5%95%8F%E9%A1%8C-6-abc-060-b---choose-integers-%E6%94%B9%E9%A1%8C%E5%85%83%E3%81%AF-200-%E7%82%B9)の6-1 ベズーの等式のセクションで発見できた。

</details>


<details><summary>コード</summary>

```python
# A, B の最大公約数を返す関数
def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)

def main():
    A, B, C = map(int, input().split())
    g = GCD(A, B)
    if C%g == 0:
        print("YES")
    else:
        print("NO")

main()
```

</details>

## 010. Together 

https://atcoder.jp/contests/abc072/tasks/arc082_a

<details><summary>コード</summary>

```python
from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in A:
        d[i] += 1
    
    ans = 0
    key_list = list(d.keys())
    
    for k in key_list:
        cnt = d[k] + d[k-1] + d[k+1]
        ans = max(ans, cnt)
    
    print(ans)

main()
```

</details>


## 011. Checkpoints 

https://atcoder.jp/contests/abc057/tasks/abc057_b

<details><summary>コード</summary>

```python
def calc_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def main():
    N, M = map(int, input().split())
    students = [list(map(int, input().split())) for _ in range(N)]
    points = [list(map(int, input().split())) for _ in range(M)]

    for person in students:
        dist = 10**18
        checkpoint = 0
        for p in range(len(points)):
            if (d := calc_dist(person[0], person[1], points[p][0], points[p][1])) < dist:
                dist = d
                checkpoint = p+1
        print(checkpoint)
    

main()
```

</details>


## 012. Grid Compression 

https://atcoder.jp/contests/abc107/tasks/abc107_b

<details><summary>コード</summary>

```python
def solve():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    row_list = set()
    col_list = set()

    for row in range(H):
        for col in range(W):
            if A[row][col] == "#":
                row_list.add(row)
                col_list.add(col)
    
    for r in range(H):
        ans = ""
        for c in range(W):
            if r in row_list and c in col_list:
                ans += A[r][c]
        if ans == "":
            continue
        else:
            print(ans)

solve()
```

</details>

## 013. Traveling 

https://atcoder.jp/contests/abc086/tasks/arc089_a


<details><summary>コード</summary>

```python
def check(x1,y1,x2,y2,t1,t2):
    dist = abs(x1-x2)+abs(y1-y2)
    time = t2-t1
    if dist > time:
        return False
    elif (time-dist) % 2 == 1:
        return False
    return True


def main():
    N = int(input())
    prev_t = 0
    prev_x = 0
    prev_y = 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        if check(prev_x, prev_y, x, y, prev_t, t):
            prev_x = x
            prev_y = y
            prev_t = t
        else:
            return False
    
    return True 

if main():
    print("Yes")
else:
    print("No")


```

</details>


## 014. Grid Repaingting 2

https://atcoder.jp/contests/abc096/tasks/abc096_c


<details><summary>コード</summary>

```python
def main():
    dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    for row in range(H):
        for col in range(W):
            if S[row][col] == "#":
                flag = False
                for r, c in dir:
                    adj_r = row + r
                    adj_c = col + c
                    if (0 <= adj_r < H and\
                        0 <= adj_c < W and\
                            S[adj_r][adj_c] == "#"):
                        flag = True
                
                if not flag: return flag 
                        
    
    return True

if main():
    print("Yes")
else:
    print("No")
```

</details>

## 015. KEYENCE String 

https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b

<details><summary>コード</summary>

```python
def main():
    S = list(input())
    for i in range(len(S)):
        for j in range(i, len(S)):
            bef_i = S[:i]
            aft_j  =S[j:]
            if "".join(bef_i + aft_j) == "keyence":
                return True
    
    return False

if main():
    print("YES")
else:
    print("NO")
```

</details>

## 016. Bugged 


https://atcoder.jp/contests/abc063/tasks/arc075_a

<details><summary>感想</summary>

点数がすべて5の倍数と勘違いをしていたせいで３WAほど積んでしまった。

</details>

<details><summary>コード</summary>

```python
def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = int(input())
        S.append(s)

    S_sum = sum(S)

    non_zero = []
    for i in S:
        if i % 10 != 0:
            non_zero.append(i)
    
    if S_sum % 10 != 0:
        print(S_sum)
    else:
        if len(non_zero) > 0:
            S_sum -= min(non_zero)
            print(S_sum)
        else:
            print(0)

main()
```

</details>


## 017. Sentou 

https://atcoder.jp/contests/abc060/tasks/arc073_a

<details><summary>コード</summary>

```python
def main():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))
    end_time = T
    total_time = T

    for i in range(1, N):
        if t[i] < end_time:
            total_time += T - (end_time - t[i])
            end_time = t[i] + T
        else:
            end_time = t[i] + T
            total_time += T
        
    print(total_time)

main()
```

</details>

## 018. Takahashi's information

https://atcoder.jp/contests/abc088/tasks/abc088_c

<details><summary>ポイント</summary>

証明も何もできていないコードを投げたら通りました。
多分嘘解法です。解説を読んでください。

</details>


<details><summary>コード</summary>

```python
def main():
    C = [list(map(int, input().split())) for _ in range(3)]

    a1B = sum(C[0])
    a2B = sum(C[1])
    a3B = sum(C[2])

    b1A = sum([C[i][0] for i in range(3)])
    b2A = sum([C[j][0] for j in range(3)])
    b3A = sum([C[k][0] for k in range(3)])

    if abs(a1B-a2B)%3 != 0:
        return False
    if abs(a2B-a3B)%3 != 0:
        return False
    if abs(a1B-a3B)%3 != 0:
        return False
    if abs(b1A-b2A)%3 != 0:
        return False
    if abs(b1A-b3A)%3 != 0:
        return False
    if abs(b2A-b3A)%3 != 0:
        return False
    

    cross = C[0][0] + C[1][1] + C[2][2]
    if cross * 3 != (sum(C[0])+sum(C[1])+sum(C[2])):
        return False
    
    return True 

if main():
    print("Yes")
else:
    print("No")
    
    
```

</details>


## 019. RGB Boxes 

https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b


<details><summary>コード</summary>

```python
def main():
    R, G, B, N = map(int, input().split())
    cnt = 0

    for red in range(3001):
        for green in range(3001):
            if N-red*R-green*G >= 0 and (N-red*R-green*G)%B == 0:
                cnt += 1
    
    print(cnt)

main()
```

</details>


## 020. Write and Erase 

https://atcoder.jp/contests/abc073/tasks/abc073_c

