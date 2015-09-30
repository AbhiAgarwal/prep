from collections import deque
import time

class Node(object):
    """Represents a node."""

    def __init__(self, name):
        self.name = name
        self._visited = 0
        self.discovery_time = None
        self.finishing_time = None

    def neighbors(self, adjacency_list):
        return adjacency_list[self]

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value):
        if value == 1:
            self.discovery_time = time.clock()
        elif value == 2:
            self.finishing_time = time.clock()

        self._visited = value

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

def breadth_first_search(Graph, Nodes):
    for node in Nodes:
        node.visited = 0

    for node in Nodes:
        if node.visited == 0:
            breadth_first_search_visit(Graph, node)


def breadth_first_search_visit(Graph, node):
    node.visited = 1
    queue = deque([node])

    while True:
        try:
            u = queue.popleft()
        except IndexError:
            break

        for neighbor in u.neighbors(Graph):
            if neighbor.visited == 0:
                neighbor.visited = 1
                queue.append(neighbor)
        node.visited = 2

Nodes = [Node(i) for i in range(10)]

Graph = {
    Nodes[0]: [Nodes[5], Nodes[3]],
    Nodes[1]: [Nodes[8], Nodes[3]],
    Nodes[2]: [Nodes[5]],
    Nodes[3]: [Nodes[9], Nodes[8]],
    Nodes[4]: [Nodes[5], Nodes[2]],
    Nodes[5]: [Nodes[9]],
    Nodes[6]: [Nodes[9]],
    Nodes[7]: [Nodes[5], Nodes[2], Nodes[6]],
    Nodes[8]: [Nodes[9], Nodes[4]],
    Nodes[9]: [Nodes[0], Nodes[1]],
}

breadth_first_search(Graph, Nodes)
for node in sorted(Nodes, key=lambda obj: obj.finishing_time):
    print('\t {}'.format(node))
