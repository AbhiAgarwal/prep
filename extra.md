## Extra questions

- Difference between space complexity and auxiliary space? [Answer](http://functionspace.com/topic/241/Difference-between-space-complexity-and-auxiliary-space-)

    - Auxiliary space is extra space or temporary space used by the algorithm, which is mostly used in algorithm where we use swapping or temporary variables.
    - The Space complexity means total space taken by the algorithm with respect to input size.
    - Space complexity calculated by both auxiliary space and space used by the input.
    - For example:
        - If we want to compare standard sorting algorithm on the basis of then auxiliary space would be better criteria than space complexity. Merge sort uses O(n) auxiliary space, where Insertion sort and Heap sort uses O(1) auxiliary space.
    - Merge sort requires Ω(n) but Heap sort requires only a constant amount.
    - Space complexity of all these sorting algorithm is O(n) though.

- What is Big Omega (Ω):
    - Big Omega is the lower bound to a function.
    - Big O is the upper bound to a function.