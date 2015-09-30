# -*- coding: utf-8 -*-

__author__ = 'Nikolai Tschacher'
__version__ = '0.1'
__contact__ = 'admin@incolumitas.com'


import time
from collections import deque

"""
This is just a little representation of two basic graph traversal methods.

    - Depth-First-Search
    - Breadth-First-Search

It's by no means meant to be fast or performant. Rather it is for educational
purposes and to understand it better for myself.
"""


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


# Let's define our sample graph and represent it in an adjacency list.
# This means that for every node, we store the outgoing edges in a list.

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

"""
Depth-First-Search

Running time: O(|V| + |E|)
"""

def depth_first_search(Graph, Nodes):
    for node in Nodes:
        node.visited = 0

    for node in Nodes:
        if node.visited == 0:
            depth_first_search_visit(Graph, node)


def depth_first_search_visit(Graph, node):
    node.visited = 1
    for neighbor in node.neighbors(Graph):
        if neighbor.visited == 0:
            depth_first_search_visit(Graph, neighbor)
    node.visited = 2


"""
Breadth-First-Search
"""

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


def print_topological(Nodes):
    print('Toplogical sort of the Graph:')
    # prints a topological sort
    for node in sorted(Nodes, key=lambda obj: obj.finishing_time):
        print('\t {}'.format(node))


if __name__ == '__main__':
    print('Using Depth-First-Search')
    # should print each node exactly once
    depth_first_search(Graph, Nodes)
    print_topological(Nodes)

    print('\n')

    # the same buth with Breadth-First-Search
    print('Using Breadth-First-Search')
    breadth_first_search(Graph, Nodes)
    print_topological(Nodes)