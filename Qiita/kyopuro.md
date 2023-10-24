

## 初めに
こんにちは。AtC茶コーダーPythonistaです。かれこれ茶で停滞してから4か月が経ちそうな勢いですが、最近は安定して茶/緑のボーダーくらいのパフォーマンスをとれるようになってきました。これが「安定して緑パフォ」になれば緑コーダーへの道もそう遠くはないのでしょう。

ここらで一度自身の競プロへの取り組み方を振り返ろうと思ったので、自分が取り入れてとても楽になったテクニック、コンテスト中に忘れがちだから気を付けておきたいこと等を備忘録程度に書きます。

## 取り入れて楽になったモノ

### 入力の関数化
7月くらいまでは毎回律義に```map(int, input().split())```なんて打ってましたが、長いし打ち間違いも多発するのでこの際全部関数にしました。とても楽です。

```python
import sys
input = sys.stdin.buffer.readline
def isint(): return int(input())
def ismap(): return map(int, input().split())
def issmap(): return map(str, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]
# indexの関係で全ての要素から1引いて扱いたいときに使います
def iszero(): return list(map(lambda x: int(x) - 1, input().split()))
```

これを毎回置いておくだけでストレスがだいぶなくなりました。```isgraph```以降はほとんどコンテスト中に使ったことはありませんが、自分でグラフ問題の練習をしているときにはよく使います。

使用例
```python
a,b,c = ismap()
list_of_strings = islist()
list_of_numbers = list(ismap())
```

### 頻出ライブラリを先に用意しておく

これも入力の関数化と似たようなものですが、使いたいライブラリがあってもいちいち調べるのは面倒なので、一度でも使ったものは基本的に最初から持っておくようにしています。今のところは以下の通りです。

```python
from collections import deque, Counter, defaultdict
from operator import itemgetter 
from bisect import bisect_right, bisect_left 
from itertools import combinations, permutations, accumulate, product, groupby
import heapq
# from numpy import base_repr
from copy import deepcopy
import sys
# sys.setrecursionlimit(10**9)
from math import gcd, log2, log10
from functools import lru_cache
# @lru_cache(maxsize=None)
```

特に```collections```と```itertools```はとても優秀なので愛用しています。```numpy```はPyPyでは使えないので特に注意が必要、これで数回コンテスト中に余計なREを積んだことがあります。

### その他関数

Python使っている方は分かると思いますが```math```ライブラリちょっと怖くて使えないですよね。誤差が怖いので、```ceil```関数は自前のモノを用意します。それ以外にも便利な関数をちょこちょこ作っておきます。

切り捨て除算を用いた```ceil```関数です。
```python
def my_ceil(a, b):
    return (-a // b) * (-1)
```

AtCのPythonのバージョンでは```math```の```lcm```は使えず、そのくせ最小公倍数は頻出なので持っておくと便利です。
```python
def my_lcm(a, b):
    return a * b // gcd(a, b)
```

```main```関数で```bool```を返すように定義するとき、解答の際はこれがあるとスムーズです。
```python
def ans_bool(func):
    if func: print("Yes")
    else: print("No")
```
二項係数の計算は畳みこみ関数を使用すると簡潔に記述できます。
```python
from operator import mul
from functools import reduce

def nCr(n,r):
    if n < 1: return 0
    if n < r: return 0
    r = min(n-r,r)
    if r == 0: return 1
    nume = reduce(mul, range(n-r+1, n))
    denom = reduce(mul, range(1, r+1))
    return nume // denom
```

## コンテスト中に忘れがちなこと

### 迷路系のBFS
迷路系のBFSは、飛び出していないか＋壁がないか＋訪問済みかを全てチェックしないといけないので大変です。

### 累積和
累積和を使うときは尺取り法等を使って部分和を求めることが多いですが、先頭に$0$を```insert```しておかないと初項が取れないので注意が必要です。僕は一回これを知らずに6ペナ積みました。
```python
from itertools import accumulate
a = list()
accumualted_a = list(accumulate(a))
accumulated_a.insert(0)
```

### グラフ構築

#### 盤面をグラフに変換
例えば$n\times m$マスの盤面でBFSをするとき、それぞれのマス目に番号を付けたいことがあります。$i$行$j$列目という情報から数字を割り当てようとすると、

