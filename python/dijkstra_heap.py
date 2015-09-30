import heapq
 
 
class PriorityQueue(object):
    """Priority queue based on heap, capable of inserting a new node with
    desired priority, updating the priority of an existing node and deleting
    an abitrary node while keeping invariant"""
 
    def __init__(self, heap=[]):
        """if 'heap' is not empty, make sure it's heapified"""
 
        heapq.heapify(heap)
        self.heap = heap
        self.entry_finder = dict({i[-1]: i for i in heap})
        self.REMOVED = '<remove_marker>'
 
    def insert(self, node, priority=0):
        """'entry_finder' bookkeeps all valid entries, which are bonded in
        'heap'. Changing an entry in either leads to changes in both."""
 
        if node in self.entry_finder:
            self.delete(node)
        entry = [priority, node]
        self.entry_finder[node] = entry
        heapq.heappush(self.heap, entry)
 
    def delete(self, node):
        """Instead of breaking invariant by direct removal of an entry, mark
        the entry as "REMOVED" in 'heap' and remove it from 'entry_finder'.
        Logic in 'pop()' properly takes care of the deleted nodes."""
 
        entry = self.entry_finder.pop(node)
        entry[-1] = self.REMOVED
        return entry[0]
 
    def pop(self):
        """Any popped node marked by "REMOVED" does not return, the deleted
        nodes might be popped or still in heap, either case is fine."""
 
        while self.heap:
            priority, node = heapq.heappop(self.heap)
            if node is not self.REMOVED:
                del self.entry_finder[node]
                return priority, node
        raise KeyError('pop from an empty priority queue')
 
 
def dijkstra(source, pq, edges):
    """Returns the shortest paths from the source to all other nodes.
    'edges' are in form of {head: [(tail, edge_dist), ...]}, contain all
    edges of the graph, both directions if undirected."""
 
    size = len(pq.heap) + 1
    processed = 1
    uncharted = set([i[1] for i in pq.heap])
    shortest_path = {}
    shortest_path1 = 0
    while size > len(processed):
        min_dist, new_node = pq.pop()
        processed.append(new_node)
        uncharted.remove(new_node)
        shortest_path[new_node] = min_dist
        for head, edge_dist in edges[new_node]:
            if head in uncharted:
                old_dist = pq.delete(head)
                new_dist = min(old_dist, min_dist + edge_dist)
                pq.insert(head, new_dist)
    return shortest_path
