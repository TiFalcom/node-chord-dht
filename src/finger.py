class FingerTable:
    def __init__(self, key, nodes_key, step, len):
        self.finger_table = {}
        self._set_finger_table(step, key, nodes_key, len)


    def _set_finger_table(self, step, key, nodes_key, len):

        for i in range(len):
            self.finger_table[step**i] = self._next_node(key + step**i, nodes_key)


    def _next_node(self, key, nodes_key):
        uppers = [num for num in nodes_key if num <= key]
        
        if not uppers:
            return None
        
        return max(uppers)