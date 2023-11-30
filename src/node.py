from src.finger import FingerTable
from enum import Enum

class Status(Enum):
    FULL_JUMP = 1
    SINGLE_JUMP = 2
    SEQUENTIAL = 3


class Node:
    def __init__(self, hash_table, key):
        self.key = key
        self.hash_table = hash_table


    def set_finger_table(self, nodes, len_finger, len_ring, step=2):
        node_keys = []
        for node in nodes:
            node_keys.append(node.key)
        self.finger_table = FingerTable(self.key, node_keys, step, len_finger, len_ring)


    def set_next_node(self, next):
        self.next_node = next

    
    def find_node_jump(self, key, nodes, steps=1, mode=Status.SINGLE_JUMP):
        lowers = [num for num in self.finger_table.finger_table.values() if (num is not None) and (num <= key)]

        if lowers == []:
            node_key = None
        else:
            node_key = max(lowers)

        if self.key == key:
            return steps

        if mode == Status.SEQUENTIAL:
            #nodes[self.next_node].find_node_jump(key, nodes, steps+1)
            return self._find_node_seq(key, nodes, steps+1)
        
        elif mode == Status.SINGLE_JUMP:
            if node_key == None:
                return nodes[max(self.finger_table.finger_table.values())].find_node_jump(key, nodes, steps+1, mode=Status.SEQUENTIAL)
            return nodes[node_key].find_node_jump(key, nodes, steps+1, mode=Status.SEQUENTIAL)
        else:
            if node_key == None:
                return nodes[max(self.finger_table.finger_table.values())].find_node_jump(key, nodes, steps+1, mode)
            return nodes[node_key].find_node_jump(key, nodes, steps+1, mode)
        

    def _find_node_seq(self, key, nodes, steps):
        if nodes[self.next_node].key == key:
            return steps
        
        return nodes[self.next_node]._find_node_seq(key, nodes, steps+1)

    def download_file(self):
        pass


    
