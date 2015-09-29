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

- x[-1] is the last element. You can work backwards by doing x[-2], etc.

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
    - 

### Development Practices and Open-Ended Discussion
