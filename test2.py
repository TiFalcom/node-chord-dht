from src.node import Node, Status
import pandas as pd
import os
import sys
sys.setrecursionlimit(15000)

nodes = []

for index in range(1000):
    nodes.append(Node({'a' : ['oi']}, index))


for index, node in enumerate(nodes):
    node.set_finger_table(nodes, 5, 1000)
    #print(index, node.finger_table.finger_table)
    if index == len(nodes)-1:
        node.set_next_node(0)
    else:
        node.set_next_node(index+1)

n = 1000

df = pd.read_csv(os.path.join('data', 'aleatorios', f'aleatorio_0_{n-1}', f'0_{n-1}.csv'), delimiter=';')
df['distance'] = df['destino'] - df['origem']

for status in Status:
    print(status)
    df[f'STEPS_{status}'] = 0
    for index, row in df.iterrows():
        steps = nodes[row['origem']].find_node_jump(row['destino'], nodes, 1, status)
        df.loc[index, f'STEPS_{status}'] = steps

df.to_csv('data/aleatorios/aleatorio_0_999/resultado.csv')
