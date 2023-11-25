from src.node import Node
import os

nodes = []

for index in range(1000):
    nodes.append(Node({'a' : ['oi']}, index))


for index, node in enumerate(nodes):
    node.set_finger_table(nodes[index+1:], 5)
    if index == len(nodes)-1:
        node.set_next_node(0)
    else:
        node.set_next_node(index+1)


print('Encontrar Peer 910 partindo do Peer 1 com single jump')
print(nodes[1].find_node_jump(910, nodes, 1,'single_jump'))

print('Encontrar Peer 910 partindo do Peer 1 com max jumps')
print(nodes[1].find_node_jump(910, nodes, 1,'max_jump'))

