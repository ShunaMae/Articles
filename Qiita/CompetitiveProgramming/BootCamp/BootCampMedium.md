
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


<details><summary>コード</summary>

```python
from collections import defaultdict 
from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0 
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)

    for i in A:
        d[i] += 1
    
    cnt = 0
    for v in d.values():
        if v >= 2:
            cnt += cmb(v, 2)
    
    for j in A:
        # print(j, 'j', cnt, d[j])
        ans = cnt
        if d[j] >= 3:
            ans -= cmb(d[j], 2)
            ans += cmb(d[j]-1, 2)
        elif d[j] == 2:
            ans -= 1
        print(ans)

main()



```

</details>


## 021. Banned K

https://atcoder.jp/contests/abc159/tasks/abc159_d

<details><summary>コード</summary>

```python
from collections import defaultdict 
from operator import mul
from functools import reduce

def cmb(n,r):
    if n <= 1: return 0 
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)

    for i in A:
        d[i] += 1
    
    cnt = 0
    for v in d.values():
        if v >= 2:
            cnt += cmb(v, 2)
    
    for j in A:
        # print(j, 'j', cnt, d[j])
        ans = cnt
        if d[j] >= 3:
            ans -= cmb(d[j], 2)
            ans += cmb(d[j]-1, 2)
        elif d[j] == 2:
            ans -= 1
        print(ans)

main()



```

</details>

## 022. Dice and Coin 

https://atcoder.jp/contests/abc126/tasks/abc126_c

<details><summary>コード</summary>

```python

def main():
    N, K = map(int, input().split())

    prob = 0

    for i in range(1, N+1):

        cnt = 0
        n = i
        while True:
            if n < K:
                n *= 2 
                cnt += 1
            else:
                break 
        
        prob += (1/N) * (1/2) ** cnt
    
    print(prob)

main()

```

</details>


## 023. Guess The Number 

https://atcoder.jp/contests/abc157/tasks/abc157_c

<details><summary>供養</summary>

馬鹿正直に書いたが一つWAが取れなくてわからないので供養する

```python
def main():
    N, M = map(int, input().split())
    num = [(-1) for _ in range(N)]
    for _ in range(M):
        s, c = map(int, input().split())
        if num[s-1] == -1 or num[s-1] == c:
            num[s-1] = c
        else:
            print(-1)
            return 
    
    if N == 1 and num[0] == 0:
        print(0)
        return 
    
    for i in range(N):
        if i == 0:
            if num[0] == -1:
                num[0] = 1
            elif num[0] == 0:
                print(-1)
                return
        else:
            if num[i] == -1:
                num[i] = 0
    
    print("".join([str(z) for z in num]))
    return 

main()
           
```

</details>


<details><summary>コード</summary>

```python

def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    start_N = [0, 10, 100]

    for i in range(start_N[N-1], 10**N):
        num = list(str(i))
        flag = True
        for j in range(M):
            s, c = S[j][0], S[j][1]
            if num[s-1] != str(c):
                flag = False
                break
        if flag:
            print(i)
            return
    
    print(-1)
    return

main()      
```

</details>


## 024. A+...+B Problem

https://atcoder.jp/contests/agc015/tasks/agc015_a


<details><summary>コード</summary>

```python

def main():
    N, A, B = map(int, input().split())

    # check A < B
    if A > B:
        print(0)
        return 
    
    min_sum = (N-1)*A+B
    max_sum = (N-1)*B+A
    print(max_sum-min_sum+1 if (max_sum-min_sum) >= 0 else 0)
    return

main()
```

</details>


## 025. Not so Diverse 

https://atcoder.jp/contests/abc081/tasks/arc086_a

<details><summary>コード</summary>

```python
from collections import defaultdict

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in A:
        d[i] += 1 
    value_list = sorted(list(d.values()), reverse=True)
    ans = 0
    for j in range(len(value_list)):
        if j >= K:
            ans += value_list[j]
    
    print(ans)

main()


```

</details>


## 026. Sorted Arrays 

https://atcoder.jp/contests/agc013/tasks/agc013_a


<details><summary>コード</summary>

```python
# 尺取り

from collections import deque
def main():
    N = int(input())
    A = deque(list(map(int, input().split())))

    que = deque([])
    flag = 0 # 0: Undetermined, 1: Increasing, 2: Decreasing 
    cnt = 0

    cur = A.popleft()

    while True:

        if len(A) == 0:
            break

        next = A.popleft()

        if flag == 0: # Undetermined 
            if cur < next: # incresing 
                flag = 1 
                que.append(cur)
                cur = next
            elif cur == next:
                que.append(cur)
                cur = next 
            else:
                # cur > next # decresing 
                flag = 2
                que.append(cur)
                cur = next 
        
        elif flag == 1: # increasing 
            if cur <= next: # increasing 
                que.append(cur)
                cur = next
            else:
                cnt += 1
                que.append(cur)
                cur = next
                flag = 0
        
        else:
            # flag == 2 decreasing 
            if cur >= next: 
                que.append(cur)
                cur = next
            else:
                cnt += 1
                que.append(cur)
                cur = next
                flag = 0

    print(cnt+1)

main()
```

</details>


## 027. Prefix and Suffix 


https://atcoder.jp/contests/agc006/tasks/agc006_a

<details><summary>コード</summary>

```python

def main():
    N = int(input())
    s = list(input())
    t = list(input())

    cnt = 0
    for i in range(N):
        if s[i:] == t[:N-i]:
            cnt = max(cnt, len(s[i:]))
    
    print(2*N-cnt)

main()

```

</details>

## 028. Dice in Line 


https://atcoder.jp/contests/abc154/tasks/abc154_d

<details><summary>コード</summary>

```python

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = [0]
    for i in range(N):
        Q.append(Q[i]+P[i])

    s = 0
    for i in range(1, N-K+2):
        temp = Q[i+K-1] - Q[i-1]
        s = max(s, temp)

    
    print((s+K) / 2)
    
main()

```

</details>

## 029. Two Anagrams 

https://atcoder.jp/contests/abc082/tasks/abc082_b

<details><summary>コード</summary>

```python

def main():
    s = "".join(sorted(list(input())))
    t = "".join(sorted(list(input()), reverse=True))

    if s < t:
        print("Yes")
    else:
        print("No")


main()
```

</details>


## 030. Flip, Flip, and Flip...

https://atcoder.jp/contests/abc090/tasks/arc091_a


<details><summary>コード</summary>

```python

def main():
    N, M = map(int, input().split())

    if N==M==1:
        print(1)
    elif N==1 or M==1:
        print(max(N,M)-2)
    else:
        print((N-2)*(M-2))

main()
```

</details>


## 0031. 4-adjacent 

https://atcoder.jp/contests/abc069/tasks/arc080_a

<details><summary>コード</summary>

```python

def main():
    N = int(input())
    A = list(map(int, input().split()))
    odd = 0
    four = 0
    even = 0

    for i in A:
        if i % 4 == 0:
            four += 1
        elif i % 2 == 1:
            odd += 1
        else:
            even += 1
    
    if four >= odd:
        print("Yes")
    elif four == odd-1 and even == 0:
        print("Yes")
    else:
        print("No")
main()
```

</details>


## 032. Otoshidama 

https://atcoder.jp/contests/abc085/tasks/abc085_c


<details><summary>コード</summary>

```python

def main():
    N,Y = map(int, input().split())

    for i in range(N+1):
        for j in range(N+1):
            if N-i-j >= 0 and 10000*i+5000*j+1000*(N-i-j) == Y:
                print(i, j, N-i-j)
                return 
    
    print(-1, -1, -1)
    return 

main()
```

</details>

## 032. Unhappy Hacking (ABC Edit)

https://atcoder.jp/contests/abc043/tasks/abc043_b

<details><summary>コード</summary>

```python
from collections import deque

def main():
    S = list(input())
    A = deque([])

    for i in S:
        if i == "0":
            A.append("0")
        elif i == "1":
            A.append("1")
        else:
            if len(A) > 0:
                A.pop()
            else:
                continue
    
    ans = "".join(list(A))
    print(ans)

main()
```

</details>


## 034. Minimization 

https://atcoder.jp/contests/abc101/tasks/arc099_a


<details><summary>コード</summary>

```python
def my_ceil(N, W):
    return (-(-N//W))

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = my_ceil(N-1, K-1)
    print(ans)

main()

```

</details>

## 035. Anti-Division 

https://atcoder.jp/contests/abc131/tasks/abc131_c

<details><summary>コード</summary>

```python
import math 
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

def main():
    A, B, C, D = map(int, input().split())
    cd = my_lcm(C, D)
    less_A = A-1

    a_num = (less_A//C) + (less_A//D) - (less_A//cd)
    b_num = (B//C) + (B//D) - (B//cd)

    
    print(B-A+1-b_num+a_num)

main()
```

</details>

## 036. Skip 

https://atcoder.jp/contests/abc109/tasks/abc109_c

<details><summary>ポイント</summary>

リストの全要素の最大公約数が`functools`の`reduce`関数を使うと簡単に求められるようです。

[参考ブログ](https://flytech.work/blog/21511/)

</details>


<details><summary>コード</summary>

```python
from math import gcd
from functools import reduce 

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x = sorted(x)
    gap = []
    ans = 0
    for i in range(1, len(x)):
        gap.append(x[i]-x[i-1])

    ans = reduce(gcd, gap)

    print(ans)

main()
```

</details>



## 037. Grand Garden 

https://atcoder.jp/contests/abc116/tasks/abc116_c


<details><summary>コード</summary>

```python
def main():
    N = int(input())
    h = list(map(int, input().split()))

    h.insert(0,0)
    h.append(0)

    cnt = 0
    for i in range(1, len(h)):
        cnt += abs(h[i]-h[i-1])
    
    print(cnt // 2)

main()
```

</details>

## 038. Problem Set

https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_b


<details><summary>ポイント</summary>

`sortedcontainers`を使うととてもシンプルに実装できます。

[参考記事](https://qiita.com/Shirotsume/items/706742162db68c481c3c)

</details>

<details><summary>コード</summary>

```python
from sortedcontainers import SortedSet, SortedList, SortedDict

def main():
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))

    S = SortedList(D)

    for i in range(M):
        if T[i] in S:
            S.discard(T[i])
        else:
            print("NO")
            return 
    
    print("YES")
    return 

main()  
```

</details>


## 039. When I hit my pocket...

https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_c


<details><summary>コード</summary>

```python
def main():
    K, A, B = map(int, input().split())

    if A >= B-2:
        print(K+1)
    else:
        if K + 1 >= A:
            print(((K-A+1)//2) * (B-A) + (A+(K-A+1-(K-A+1)//2*2) if (K-A+1)%2 != 0 else A))
        else:
            print(K+1)
            

main()
```

</details>

## 040. Streamline 

https://atcoder.jp/contests/abc117/tasks/abc117_c

<details><summary>コード</summary>

```python
def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))

    gap = []
    for i in range(1, M):
        gap.append(abs(X[i]-X[i-1]))
    
    if N >= M:
        print(0)
    else:
        ans = 0
        gap = sorted(gap)
        for i in range(M-N):
            ans += gap[i]
        
        print(ans)


main()
```

</details>

## 041. Shrinking 

https://atcoder.jp/contests/agc016/tasks/agc016_a

解説AC


<details><summary>コード</summary>

```python

```

</details>



## 042. Evilator 

https://atcoder.jp/contests/agc015/tasks/agc015_b


<details><summary>コード</summary>

```python
def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "U":
            # going up
            ans += len(S)-(i+1)
            # going down
            ans += 2 * i
        else:
            # going up
            ans += 2 * (len(S)-(i+1))
            ans += i
    
    print(ans)

main()
```

</details>

## 043. Go Home 

https://atcoder.jp/contests/abc056/tasks/arc070_a

<details><summary>コード</summary>

```python

def main():
    X = abs(int(input()))
    i = 0

    while True:
        if (0+i) * (i-0+1) // 2 >= X:
            break 
        i += 1
    
    print(i)

main()


```

</details>

## 044. pushpush

https://atcoder.jp/contests/abc066/tasks/arc077_a

<details><summary>コード</summary>

```python
from collections import deque

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = deque([])

    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                b.append(a[i])
            else:
                b.appendleft(a[i])
    else:
        for i in range(n):
            if i % 2 == 0:
                b.appendleft(a[i])
            else:
                b.append(a[i])
    
    print(*b)

main()
```

</details>

## 045. Scc puzzle 

https://atcoder.jp/contests/abc055/tasks/arc069_a


<details><summary>コード</summary>

```python

def main():
    N, M = map(int, input().split())
    ans = 0

    if N*2 <= M:
        ans += N
        M -= N*2
    else:
        print(M//2)
        return 
    
    ans += M//4

    print(ans)

main()
```

</details>


## 046. Palindrome-phobia 

https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b


<details><summary>コード</summary>

```python
def main():
    S = input()
    a = S.count('a')
    b = S.count('b')
    c = S.count('c')

    if abs(a-b) <= 1 and abs(b-c) <= 1 and abs(a-c) <= 1:
        print("YES")
    else:
        print("NO")

main()

```

</details>


## 047. Biscuits 

https://atcoder.jp/contests/agc017/tasks/agc017_a

<details><summary>コード</summary>

```python
def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))

    odd = 0
    even = 0

    for i in range(N):
        if A[i] % 2:
            odd += 1
        else:
            even += 1
    
    if odd == 0:
        if P == 1:
            print(0)
        else:
            print(2**even)
    else: # 奇数が含まれている
        print(2**(N-1))

main()


```

</details>


## 048. Rectangle Cutting 

https://atcoder.jp/contests/abc130/tasks/abc130_c

<details><summary>コード</summary>

```python
def main():
    W, H, x, y = map(int, input().split())

    if x*2 == W and y*2 == H:
        print(H*W/2, 1)
    else:
        print(H*W/2, 0)

main()
```

</details>

## 049. Make a Rectangle 

https://atcoder.jp/contests/abc071/tasks/arc081_a

<details><summary>コード</summary>

```python
from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = sorted(Counter(A).items(), reverse=True)
    ans = []
    for i in C:
        if i[1] >= 4:
            ans.append(i[0])
            ans.append(i[0])
        elif i[1] >= 2:
            ans.append(i[0])
    
    if len(ans) < 2:
        print(0)
    else:
        print(ans[0]*ans[1])

main()
```

</details>


## 050. Remainder Minimization 2019 

https://atcoder.jp/contests/abc133/tasks/abc133_c

<details><summary>コード</summary>

```python
def main():
    L, R = map(int, input().split())

    if R-L >= 2019:
        return 0
    
    l = L%2019
    r = R%2019

    if l >= r:
        return 0
    else:
        mod_set = set()
        for i in range(l, r+1):
            mod_set.add(i)
        
        if 0 in mod_set:
            return 0
        else:
            ans = 2019
            mod_set = list(mod_set)
            for j in range(len(mod_set)):
                for k in range(j+1, len(mod_set)):
                    ans = min(ans, (mod_set[j]*mod_set[k])%2019)
            
            return ans
        
print(main())
```

</details>