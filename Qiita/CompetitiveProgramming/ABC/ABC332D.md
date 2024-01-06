# D: Swapping Puzzle 

https://atcoder.jp/contests/abc332/tasks/abc332_d

AとBの２つの盤面が与えられ、Aの隣り合う行や列を入れ替える作業を繰り返してAをBに一致させられるかを問う問題です。

Pythonでの一般的な解は`permutations`を用いた全探索ですが、幅優先探索を用いた解法も[公式解説](https://atcoder.jp/contests/abc332/editorial/7922)で紹介されています。

今回はこの解法を見ていきます。


## 解法の軸

BFS(幅優先探索)解法の軸は、幅優先探索を使ってAからの遷移があり得る盤面を全部列挙し、最小手数を求めることにあります。

なので実質やっていることは`permutations`を用いた解法とほぼ同じです。違いはどのように遷移を全列挙するかの方法だけです。

## 最小手数の管理

まずはBFSで全列挙が可能なことを前提として、最小手数の管理の方法を考えます。一般的なBFS(やダイクストラ法)では頂点番号をインデックスとしたリスト等で管理しますが、今回のBFSは盤面から盤面へと動く上、まだどのような盤面が出てくるかわかっていないのでリストは使えません。集合に適宜訪れた頂点を格納していくこともありますが、それでは最小手数が求められないのでうまくいきません。

なので今回は辞書を使います。盤面の状態をキーとして、値に最小手数を持ちます。

競プロで辞書を使うとき、キーの存在チェックが不要なため`defaultdict`を多用しますが、今回は「キーが存在するかどうか」がその盤面への遷移が可能なのかの指標になるため、普通の`dict`を使用します。

辞書のキーにはイミュータブルなオブジェクトしか取れないため、盤面をリストからタプルに変換するための関数を定義します。

```python
def to_tuple(a: list) -> tuple:
    return tuple(tuple(r) for r in a)
```

## 前準備

辞書を作成し、`deque`を使ってキューの準備をします。

```python
from collections import deque 
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

# キーの存在判定をするために辞書を使う
# 最初の盤面(A)への最小手数は0
d = {to_tuple(A): 0}
queue = deque([A])
```


## BFSを用いた遷移先列挙

ではBFSでどのように盤面を全列挙できるのかを見ていきます。
まずは行の並び替えを全列挙する解説コードを見てみます。

```python
while len(queue) > 0:
    a = queue.popleft()

    # 行を入れ替える
    for i in range(H-1):
        b = deepcopy(a)
        b[i], b[i+1] = b[i+1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            queue.append(b)
```

最初にキューから次に見る盤面を取り出します。

deepcopyについては[こちら](https://qiita.com/Kaz_K/items/a3d619b9e670e689b6db)を参照ください。


行を上から隣同士で入れ替えていき、結果できるのが新しい盤面か確認（辞書で存在するキーか確認）、新しければ前回の盤面までの最小手数に１を足して辞書に追加、キューにも追加します。

なぜこれで行の並び替えはすべて列挙できるのかについて、順番に考えてみます。

盤面が１行のとき、並び替え方の列挙は自明に可能です。

盤面が２行であるとき、0行目と1行目を入れ替えると行の並び替えは全て列挙できます。

盤面が３行であるときを考えます。最初のfor-loopでは、```a = 0行目-1行目-2行目```で0行目と1行目、1行目と2行目がまず並び替えられます。この時点で辞書の中身は以下の通りです。

```
0行目-1行目-2行目
1行目-0行目-2行目 #0-1のスワップ
0行目-2行目-1行目 #1-2のスワップ
```

続いて、```1行目-0行目-2行目```が確認されます。最初の2つの行はスワップしても元の順になるだけなので、スキップされます。

```
0行目-1行目-2行目
1行目-0行目-2行目 #0-1のスワップ
0行目-2行目-1行目 #1-2のスワップ

1行目-2行目-0行目 #0-2のスワップ
```

次の```0行目-2行目-1行目```では、新たに```2行目-0行目-1行目```が辞書に追加されます。

そして最後に```2行目-0行目-1行目```をスワップして得られる```2行目-1行目-0行目```が辞書に追加されて全列挙は終了です。

順番としては以下のようになります。

```
0行目-1行目-2行目
1行目-0行目-2行目 #0-1のスワップ
0行目-2行目-1行目 #1-2のスワップ

1行目-2行目-0行目 #0-2のスワップ

2行目-0行目-1行目 #0-2のスワップ

2行目-1行目-0行目 #0-1のスワップ
```

同様にして考えると、行数が増えても同じ方法で全列挙が可能なことがわかります。（帰納法的な証明も可能です。）

従って、この方法で行の並び替え方の全列挙と、それぞれの行の並び替え方においての列の並び替え方を同じく全列挙します。

```python
while len(queue) > 0:
    a = queue.popleft()

    # rowを入れ替える
    for i in range(H-1):
        b = deepcopy(a)
        b[i], b[i+1] = b[i+1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            queue.append(b)
    
    for j in range(W-1):
        b = deepcopy(a)
        for i in range(H):
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            queue.append(b)
```
## 答えの出力

最後にBの盤面が辞書内に存在していたらそのキーを出力し、存在していなければ-1を返して終了です。

```python
from collections import deque
from copy import deepcopy 

def to_tuple(a: list) -> tuple:
    return tuple(tuple(r) for r in a)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

# 存在しないキーを参照しないためにわざと辞書を使う
d = {to_tuple(A): 0}
queue = deque([A])

while len(queue) > 0:
    a = queue.popleft()

    # 行を入れ替える
    for i in range(H-1):
        b = deepcopy(a)
        b[i], b[i+1] = b[i+1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            queue.append(b)
    
    # 列を入れ替える
    for j in range(W-1):
        b = deepcopy(a)
        for i in range(H):
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            queue.append(b)
            
print(d[to_tuple(B)] if to_tuple(B) in d else -1)

```