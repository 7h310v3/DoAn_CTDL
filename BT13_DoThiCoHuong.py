import networkx as nx
import matplotlib.pyplot as plt

# Đồ thị có hướng
c = nx.DiGraph()
c.add_nodes_from([1,2,3,4,5])
c.add_edge(1,2)
c.add_edge(4,2)
c.add_edge(3,5)
c.add_edge(2,3)
c.add_edge(2,5)
c.add_edge(1,4)
c.add_edge(3,4)

nx.draw(c,with_labels=True)
plt.draw()
plt.show()