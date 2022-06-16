import networkx as nx
import matplotlib.pyplot as plt
#Đồ thị vô hướng
v = nx.DiGraph()
v.add_nodes_from([1,2,3,4,5])
v.add_edge(1,2)
v.add_edge(4,2)
v.add_edge(3,5)
v.add_edge(2,3)
v.add_edge(2,5)
v.add_edge(1,4)
v.add_edge(3,4)

nx.draw(v,with_labels=True, arrows=False)
plt.draw()
plt.show()