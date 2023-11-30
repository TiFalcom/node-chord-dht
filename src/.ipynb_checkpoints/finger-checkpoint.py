class FingerTable:
    def __init__(self, key, nodes_key, step, len_finger, len_ring):
        self.finger_table = {}
        self._set_finger_table(step, key, nodes_key, len_finger, len_ring)


    def _set_finger_table(self, step, key, nodes_key, len_finger, len_ring):

        for i in range(len_finger):
            if (key + step**i) >= len_ring:
                value = ((key + step**i) - (len_ring*((key + step**i)//len_ring)))
            else:
                value = (key + step**i)
            self.finger_table[step**i] = self._next_node(value, nodes_key)


    def _next_node(self, key, nodes_key):
        uppers = [num for num in nodes_key if num <= key]
        
        if not uppers:
            return None
        
        return max(uppers)