def dfs_iterative(adjLists, s):
    stack = []
    stack.append(s)
    n = len(adjLists)
    visited = []
    for i in range(0,n):
        visited.append(False)
         
    while(len(stack)>0):
        v = stack.pop()
        if(not visited[v]):
            visited[v] = True
            print v
 
            # auxiliary stack to visit neighbors in the order they appear
            # in the adjacency list
            # alternatively: iterate through the adjacency list in reverse order
            # but this is only to get the same output as the recursive dfs
            # otherwise, this would not be necessary
            stack_aux = []
            for w in adjLists[v]:
                if(not visited[w]):
                    stack_aux.append(w)
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())
                     
 
# ------------------------------------------------------------------
 
# create the graph in adjacency list representation
adjLists = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4] ]
 
# test our implementation
dfs_iterative(adjLists, 0)