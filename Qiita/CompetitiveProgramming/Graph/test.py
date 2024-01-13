# # import networkx as nx
# # import matplotlib.pyplot as plt

# # # 有向グラフの作成
# # G_directed = nx.DiGraph()
# # edges_directed = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 1)]
# # G_directed.add_edges_from(edges_directed)

# # # 有向グラフの可視化
# # plt.figure(figsize=(6, 4))
# # nx.draw(G_directed, with_labels=True, arrows=True)
# # plt.title("Directed Graph")
# # plt.show()

# # import networkx as nx
# # import matplotlib.pyplot as plt

# # G_undirected = nx.DiGraph()

# # # 頂点のリスト
# # edges_undirected = [(0, 1), (1, 2), (1, 3), (3, 4), (1, 4)]

# # G_undirected.add_edges_from(edges_undirected)

# # # グラフの可視化
# # nx.draw(G_undirected, with_labels=True, arrows=False)
# # plt.show()


# # import networkx as nx
# # import matplotlib.pyplot as plt

# # # 完全グラフの例
# # G_complete = nx.complete_graph(6)

# # # グラフの可視化
# # nx.draw(G_complete, with_labels=True)
# # plt.show()

# # import networkx as nx
# # import matplotlib.pyplot as plt

# # # 有向グラフの作成
# # G_directed = nx.DiGraph()
# # edges_directed = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]
# # G_directed.add_edges_from(edges_directed)

# # # 頂点の位置を設定
# # pos = {1: (0, 0), 2: (0.5, 0.5), 3: (1, 0), 4: (0.5, -0.5)} 

# # # 可視化
# # nx.draw(G_directed, pos, with_labels=True, arrows=True)
# # plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt

# # グラフの作成
# G_weighted = nx.DiGraph()

# # （頂点１, 頂点2, 重み）
# edges_weighted = [(1, 2, 1.5), (2, 3, 2.5), (3, 4, 3.5), (4, 1, 4.5), (1, 3, 5.0)]
# # 辺を追加
# G_weighted.add_weighted_edges_from(edges_weighted)

# # 頂点の位置の自動設定
# pos = nx.spring_layout(G_weighted)

# # グラフの可視化
# nx.draw(G_weighted, pos, with_labels=True, arrows=True)

# # 重みのラベルを追加
# edge_labels = nx.get_edge_attributes(G_weighted, 'weight')
# nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)

# plt.show()

from graphviz import Digraph

dot = Digraph(comment='The Test Flowchart')

# Add nodes
dot.node('A', 'Start')
dot.node('B', 'Step 1')
dot.node('C', 'Step 2')
dot.node('D', 'End')

# Add edges
dot.edges(['AB', 'BC', 'CD'])

# Generate the flowchart
dot.render('G:GitHub/Articles/Qitta/flowchart.gv', view=True) 