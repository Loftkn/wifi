import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as image

im = image.imread('index.png')

G=nx.fast_gnp_random_graph(2,1)

pos = nx.spring_layout(G)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_alpha(0)
ax.axis(xmin=-1,xmax=2,ymin=-1,ymax=2)

for node in G.nodes():
    x,y = pos[node]
    trans_x, trans_y = ax.transData.transform((x,y))
    fig.figimage(im,trans_x,trans_y) #could use custom image for each node

nx.draw_networkx_edges(G,pos, with_labels=True)
plt.show()
