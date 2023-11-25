from src.finger import FingerTable

class Node:
    def __init__(self, hash_table, key):
        self.key = key
        self.hash_table = hash_table


    def set_finger_table(self, nodes, len, step=2):
        node_keys = []
        for node in nodes:
            node_keys.append(node.key)
        self.finger_table = FingerTable(self.key, node_keys, step, len)


    def set_next_node(self, next):
        self.next_node = next

    
    def find_node_jump(self, key, nodes, steps=1, mode='single_jump'):
        lowers = [num for num in self.finger_table.finger_table.values() if (num is not None) and (num <= key)]

        if not lowers:
            #nodes[self.next_node].find_node_jump(key, nodes, steps+1)
            return self._find_node_seq(key, nodes, steps+1)

        node_key = max(lowers)

        if node_key == key:
            return steps
        
        if mode == 'single_jump':
            return nodes[node_key]._find_node_seq(key, nodes, steps+1)
        else:
            return nodes[node_key].find_node_jump(key, nodes, steps+1, mode)
        

    def _find_node_seq(self, key, nodes, steps):
        if nodes[self.next_node].key == key:
            return steps
        
        return nodes[self.next_node]._find_node_seq(key, nodes, steps+1)

    def download_file(self):
        pass


    
