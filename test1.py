from src.node import Node, Status
import os


lista_peers = ['C:\\Users\\diego\\OneDrive\\UFABC\\AED2\\projeto\\data\\peer1',
               'C:\\Users\\diego\\OneDrive\\UFABC\\AED2\\projeto\\data\\peer2',
               'C:\\Users\\diego\\OneDrive\\UFABC\\AED2\\projeto\\data\\peer3']

hashs = []
nodes = []


def listar_arquivos_e_pastas(diretorio):
    conteudo = os.listdir(diretorio)
    hash_table = {}
    
    for fold in conteudo:
        files = [file for file in os.listdir(os.path.join(diretorio, fold))]
        hash_table[hash(fold)] = files

    return hash_table


for index, peers in enumerate(lista_peers):
    nodes.append(Node(listar_arquivos_e_pastas(peers), index))


for index, node in enumerate(nodes):
    node.set_finger_table(nodes[index+1:], 5, 2)
    print(node.finger_table.finger_table)
    if index == len(nodes)-1:
        node.set_next_node(0)
    else:
        node.set_next_node(index+1)

print(nodes[0].find_node_jump(0, nodes, 1,Status.FULL_JUMP))

