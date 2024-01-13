# グラフを可視化したい！

みなさん、競プロの問題でわけのわからないアルゴリズムを見た時、可視化したグラフでアルゴリズムを順番に精査したくなりませんか？僕はなります。そんな時、手動で描いていますか？僕は描いていました。

もうそんなことに時間は使わない！これからはNetworkx+Matplotlibでグラフを描画しましょう。

- [グラフを可視化したい！](#グラフを可視化したい)
- [Networkxとは](#networkxとは)
- [ライブラリのインストール](#ライブラリのインストール)
- [単純無向グラフ](#単純無向グラフ)
- [単純有向グラフ](#単純有向グラフ)
- [重み付きグラフ](#重み付きグラフ)
- [完全グラフ](#完全グラフ)
- [点の位置を調整](#点の位置を調整)
- [辺の追加、削除](#辺の追加削除)
- [終わりに](#終わりに)


# Networkxとは

[Networkx](https://networkx.org/documentation/stable/index.html#citing)は、ネットワーク分析のために作られたPythonのパッケージです。グラフの作成のみならず、分析、計算まで出来ちゃいます。ダイクストラ法やベルマンフォード法等も数行で記述できますが、[時間と空間計算量を食うらしい](https://qiita.com/yH3PO4/items/ffd81081c254895939c0)ので競プロの問題で使うのはお勧めできません。

[Matplotlib](https://matplotlib.org/)は言わずと知れたグラフ描画用のパッケージです。

この記事では、Networkxでグラフを作成した後にMatplotlibでそれを描画していきます。


# ライブラリのインストール

pipでインストールします

```
pip install networkx
```

この記事のコードは、`matplotlib 3.8.2`, `networkx 3.2.1`での動作を確認しています。


# 単純無向グラフ

辺に方向性がないグラフです。`draw()`関数で矢印の引数`arrows`を`False`にすることによって描くことができます。

```python
import networkx as nx
import matplotlib.pyplot as plt

# グラフの作成
G_undirected = nx.DiGraph()

# 頂点のリスト
edges_undirected = [(0, 1), (1, 2), (1, 3), (3, 4), (1, 4)]

# グラフに辺を入れる
G_undirected.add_edges_from(edges_undirected)

# グラフの可視化
nx.draw(G_undirected, with_labels=True, arrows=False)
plt.show()
```
<br>
<br>

![undirected_graph.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/dab27c53-c9d1-9d89-d4da-99c8b9a393d8.png)


# 単純有向グラフ

辺に方向が存在するグラフです。無向グラフとほとんど違いなく描くことができます。双方向の辺は1本の矢印で表されます。矢印の向きは `頂点1 -> 頂点2` です。

```python
import networkx as nx
import matplotlib.pyplot as plt

# グラフの作成
G_directed = nx.DiGraph()

# 辺のリスト
edges_directed = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 1)]

# グラフに辺を入れる
G_directed.add_edges_from(edges_directed)

# 有向グラフの可視化
plt.figure(figsize=(6, 4))
nx.draw(G_directed, with_labels=True, arrows=True)
plt.title("Directed Graph")
plt.show()
```
![directed_graph.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/117a6ba1-fa12-0dd3-27e4-ab88f84d4927.png)


# 重み付きグラフ

基本的には普通の有向グラフと同じですが、辺を追加するときに重みも追加することができます。

今までは頂点の位置の指定は必須ではありませんでしたが、重みを描画する際に必要なので頂点の位置を自動設定しておきます。頂点の位置はカスタマイズも可能です。[点の位置を調整](#点の位置を調整)を参照してください。

```python
import networkx as nx
import matplotlib.pyplot as plt

# グラフの作成
G_weighted = nx.DiGraph()

# （頂点１, 頂点2, 重み）
edges_weighted = [(1, 2, 1.5), (2, 3, 2.5), (3, 4, 3.5), (4, 1, 4.5), (1, 3, 5.0)]
# 辺を追加
G_weighted.add_weighted_edges_from(edges_weighted)

# 頂点の位置の自動設定
pos = nx.spring_layout(G_weighted)

# グラフの可視化
nx.draw(G_weighted, pos, with_labels=True, arrows=True)

# 重みのラベルを追加
edge_labels = nx.get_edge_attributes(G_weighted, 'weight')
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)

plt.show()
```
![weighted_graph.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/7b631bc4-b99a-7708-cc9a-c5ab9cfc5c8d.png)


# 完全グラフ

全ての頂点が互いに辺を持つグラフです。

```python
import networkx as nx
import matplotlib.pyplot as plt

# 頂点が6つある完全グラフ
G_complete = nx.complete_graph(6)

# グラフの可視化
nx.draw(G_complete, with_labels=True)
plt.show()
```

![complete_graph.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/79e23747-0422-8aab-49d9-cf3e1c1fa2c0.png)


# 点の位置を調整

`draw()`関数の中で、`pos`という点の位置を指定する引数があります。辞書型で座標を渡すことができます。

```python
import networkx as nx
import matplotlib.pyplot as plt

# 有向グラフの作成
G_directed = nx.DiGraph()
edges_directed = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
G_directed.add_edges_from(edges_directed)

# 頂点の位置を設定
pos = {1: (0, 0), 2: (0.5, 0.5), 3: (1, 0), 4: (0.5, -0.5)} 

# 座標を渡して可視化
nx.draw(G_directed, pos, with_labels=True, arrows=True)
plt.show()

```
![coordinates.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2611731/eff1c988-05ac-87d9-3021-9f4c4f6a2064.png)


# 辺の追加、削除

```python
# 辺の追加
G.add_edge(0, 1)                                    
G.add_edges_from([(1, 2), (2, 3)])

# 重み付きグラフへの辺の追加
weighted_G.add_edge(1, 2, weight=3.5)
```

```python
# 辺の削除
G.remove_edge(0, 1)                    
G.remove_edges_from([(1, 2), (2, 3)])
```

# 終わりに

とりあえずこれだけ出来たらグラフの描画はできそう…？他にもやりたいことがあれば追記していきます。

