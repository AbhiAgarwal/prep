# prep

### General

**Time complexity**

- BigO -> upper bound. O(n)
- Big omega -> lower bound. Ω(n)
- Big theta -> lower and upper bound. O(n) and Ω(n)

**Amortized Time**

- Average time taken per operation, if you do many operations
- If inserting N elements takes O(N) total work. Each insertion is O(1) on average, even though some insertions take O(N) time in the worst case.

### Python

- `x[-1]` is the last element. You can work backwards by doing x[-2], etc.
- `list.sort()` works in Python

### Normal Data Structures

- Stack: pop, push, peek, isEmpty (LIFO)
- Queue: add, remove, peek, isEmpty (FIFO)

### Trees and Graphs

- Tree construction, traversal, and manipulation algorithms.
- Binary trees, n-ary trees, and trie-trees
- You should be familiar with at least one flavor of balanced binary tree, whether it's a red/black tree, a splay tree or an AVL tree, and you should know how it's implemented.
- Three basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list), and you should familiarize yourself with each representation and its pros and cons.
- Tree traversal algorithms: BFS and DFS, and know the difference between inorder, postorder and preorder traversal (for trees). 
- You should know their computational complexity, their tradeoffs, and how to implement them in real code.
- If you get a chance, study up on fancier algorithms, such as Dijkstra and A* (for graphs).

#### Binary-Tree vs Binary Search Tree

- Binary Search Tree -> all left descendants values are less than or equal to root node value. All right descendants values are greater than root node value.
- Binary Tree just means it has up to 2 children.
- Not all trees are binary trees. 
- Tree with up to 3 children is a ternary tree.

#### Binary Search Tree

- Efficiency
    - Space
        - Average: O(n)
        - Worst: O(n)
    - Search
        - Average: O(log n)
        - Worst: O(n)
    - Insert
        - Average: O(log n)
        - Worst: O(n)
    - Delete
        - Average: O(log n)
        - Worst: O(n)

#### Balanced vs. Unbalanced

- Balanced enough to ensure O(log n) times for insert and find.
- Red-Black tree or AVL tree

#### Types of Binary Trees

![Types of Binary Trees](http://www.differencebetween.com/wp-content/uploads/2011/05/DifferenceBetween_Full_Binary_Tree.jpg)

- Complete Binary Trees
    - Binary tree in which every level of the tree is fully filled (maybe not the last level).
    - The last level is filled, it is filled left to right.
- Full Binary Trees
    - Every node has either zero or two children.
    - No nodes have only one child.

![Types of Binary Trees](http://web.cecs.pdx.edu/~sheard/course/Cs163/Graphics/FullBinary.jpg)

- Perfect Binary Trees
    - Both full and complete.
    - All leaf nodes will be at the same level, and this level has the maximum number of nodes.
    - A perfect tree must have exactly `2^k - 1` nodes (where k is the number of levels).

#### AVL (cracking: 637) trees

- Self-balancing binary search tree.
- Binary search tree so -> all left descendants values are less than or equal to root node value. All right descendants values are greater than root node value.
- The new principal is that it is SELF-BALANCING.
- Properties:
    1. Stores in each node the height of the subtree rooted at this node.
    2. For any node you can check if it is height balanced:
        - The height of the left subtree and the height of the right subtree differ by no more than one. This presents situations where the tree gets too lopsided.
        - balance(n) = n.left.height - n.right.height
        - -1 <= balance(n) <= 1
- Insert:
    - When you insert the balance of some nodes might change to -2 or 2. When we're unwinding the recursive stack ,we check and fix the balance at each node. We perform rotations.
    - Rotations can either be left or right rotations. The right rotation is an inverse of the left rotation.
- Efficiency
    - Space
        - Average: O(n)
        - Worst: O(n)
    - Search
        - Average: O(log n)
        - Worst: O(log n)
    - Insert
        - Average: O(1)
        - Worst: O(log n)
    - Delete
        - Average: O(1)
        - Worst: O(log n)
- Rotation:
    - Left Right shape: Left rotation
    - Left Left shape: Right rotation
    - Right Left shape: Right rotation
    - Right Right shape: Left rotation
    - Left or Right means: For the current node is the height of the left subtree greater or the right subtree.
    - Left Left (etc.) means: For the current node is the height of the left subtree greater or the right subtree. In that subtree (Left or Right) is the height of the left subtree greater or the right subtree.

#### Red-black trees (cracking: 639)

- Efficiency
    - Space
        - Average: O(n)
        - Worst: O(n)
    - Search
        - Average: O(log n)
        - Worst: O(log n)
    - Insert
        - Average: O(1)
        - Worst: O(log n)
    - Delete
        - Average: O(1)
        - Worst: O(log n)

#### Splay trees

- Splay trees maintain efficiency by reshaping the tree in response to lookups on it
- That way, frequently-accessed elements move up toward the top of the tree and have better lookup times. The shape of splay trees is not constrained, and varies based on what lookups are performed.

#### AVL trees vs Red-black trees

- The operations to balance the trees are different, but both occur on the average in O(1) with maximum in O(log n).
- Real difference between the two is the limiting height. For a tree of size n:
    - A red-black tree's height is at most: 2*log_2(n+1)
    - An AVL tree's height is strictly less than: [some complex equation](https://upload.wikimedia.org/math/5/5/1/5510f359619e43c60ceb3b8eacf9ad24.png)

AVL trees

    - Insertion/Removal is slower. Retrieval is faster.
    - AVL trees are more rigidly balanced than red-black trees, leading to slower insertion and removal but faster retrieval.
    - For lookup-intensive applications, AVL trees are faster than red-black trees because they are more rigidly balanced.

Red Black trees

    - RB-Trees guarantee O(1) rotations per insert operation.
    - RB-Trees gain this advantage from conceptually being 2-3 trees without carrying around the overhead of dynamic node structures.
    - Physically RB-Trees are implemented as binary trees, the red/black-flags simulate 2-3 behavior.

#### [AVL trees vs Splay trees](http://stackoverflow.com/questions/7467079/difference-between-avl-trees-and-splay-trees)

AVL trees

    - One key difference between the structures is that AVL trees guarantee fast lookup (O(log n)) on each operation, while splay trees can only guarantee that any sequence of n operations takes at most O(n log n) time.
    - If you need real-time lookups, the AVL tree is likely to be better.
    - However, AVL trees are more useful in multithreaded environments with lots of lookups, because lookups in an AVL tree can be done in parallel while they can't in splay trees.

Splay trees

    - Splay trees tend to be much faster on average, so if you want to minimize the total runtime of tree lookups, the splay tree is likely to be better.
    - Splay trees support some operations such as splitting and merging very efficiently, while the corresponding AVL tree operations are more involved and less efficient.
    - Splay trees are more memory-efficient than AVL trees, because they do not need to store balance information in the nodes.
    - Because splay trees reshape themselves based on lookups, if you only need to access a small subset of the elements of the tree, or if you access some elements much more than others, the splay tree will outperform the AVL tree.
    - Finally, splay trees tend to be easier to implement than AVL trees, since the rotation logic is much easier.

Time efficiency

    - AVL tree insertion, deletion, and lookups take O(log n) time each. 
    - Splay trees have these same guarantees, but the guarantee is only in an amortized sense.
        - Any long sequence of operations will take at most O(n log n) time, but individual operations might take as much as O(n) time.

#### Binary Tree Traversal

- In-Order Traversal:
    1. Left
    2. Current node
    3. Right
- Pre-Order Traversal:
    1. Current
    2. Left
    3. Right
- Post-Order Traversal:
    1. Left
    2. Right
    3. Current

#### Binary heaps: Min-Heaps and Max-Heaps

![Binary heaps: Min-Heaps](http://algorithms.tutorialhorizon.com/files/2015/02/Delete-OR-Extract-Min-from-Heap.gif)

- Complete Binary Tree (totally filled other than the rightmost elements on the last level).
- Min heap is where each node is smaller than its children. The root is the minimum element in the tree.
- Built into Python `from heapq import heappush, heappop`

#### Trie Trees / Prefix tree

![Prefix tree](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/500px-Trie_example.svg.png)


- Null nodes (* nodes) are used to indicate complete words.
- A trie can check if a string is a valid prefix in O(K) time, where K is the length of the string.
- The term trie comes from retrieval.

### Graphs

- A tree is a type of graph. Not all graphs are trees.
- A tree is a connected graph without cycles.
- A graph is simply a collection of nodes with edges between (some of) them.
- Can be directed or undirected.

#### Three basic ways to represent a graph in memory

1. 

### Array Sorting Algorithms

![Array Sorting Algorithms](https://raw.githubusercontent.com/AbhiAgarwal/prep/master/pictures/Array-Sorting-Algorithms.png?token=ACNNWrUUI4rMuYBCTUTO_IfkukWNYKJsks5WDsUowA%3D%3D)

#### Quicksort

- 

##### When is Quicksort impractical

#### Mergesort

- Uses divide and conquer to recursively divide and sort the list
- Time Complexity: O(n log n)
- Space Complexity: O(n) Auxiliary

##### When is Mergesort impractical

##### Quicksort vs Mergesort

### Hash Tables

#### How they work

#### Be able to implement one using only arrays in your favorite language

### Other data structures

- Most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem.

### Operating Systems, Systems Programming and Concurrency

- Know about processes, threads, and concurrency issues. Know about locks, mutexes, semaphores and monitors, and how they work. Know about deadlock and livelock and how to avoid them.
- Know what resources a processes needs, a thread needs, how context switching works, and how it's initiated by the operating system and underlying hardware.
- Know a little about scheduling. The world is rapidly moving towards multi-core, so know the fundamentals of "modern" concurrency constructs.

### Coding

- Know Python well

### Recursion and Induction

- You should be able to solve a problem recursively, and know how to use and repurpose common recursive algorithms to solve new problems. 
- Conversely, you should be able to take a given algorithm and prove inductively that it will do what you claim it will do.

### Data Structure Analysis and Discrete Math

- Some interviewers ask basic discrete math questions. This is more prevalent at Google than at other companies because we are surrounded by counting problems, probability problems, and other Discrete Math 101 situations.
- Spend some time before the interview on the essentials of combinatorics and probability. You should be familiar with n-choose-k problems and their ilk – the more the better.

### System Design

- You should be able to take a big problem, decompose it into its basic subproblems, and talk about the pros and cons of different approaches to solving those subproblems as they relate to the original goal. 

### Development Practices and Open-Ended Discussion
