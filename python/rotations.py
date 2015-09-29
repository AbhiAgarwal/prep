# Left tree: ((A, P, B), Q, C)        Right tree: (A, P, (B, Q, C))

'''
Using the terminology of Root for the parent node of the subtrees to rotate, 
Pivot for the node which will become the new parent node, RS for rotation side
upon to rotate and OS for opposite side of rotation. In the above diagram for
the root Q, the RS is C and the OS is P. The pseudo code for the rotation is:

Pivot = Root.OS
Root.OS = Pivot.RS
Pivot.RS = Root
Root = Pivot

---

Right Rotation of node Q:

Let P be Q's left child.
Set Q's left child to be P's right child.
[Set P's right-child's parent to Q]
Set P's right child to be Q.
[Set Q's parent to P]

Q -> left child -> P right now
Q -> left child -> P right child
P -> right child parent -> Q
P -> right child -> Q
Q -> parent -> P

--- 

Left Rotation of node P:

Let Q be P's right child.
Set P's right child to be Q's left child.
[Set Q's left-child's parent to P]
Set Q's left child to be P.
[Set P's parent to Q]

'''

def right_rotation(treenode):
    left, Q, C = treenode
    A, P, B = left
    return (A, P, (B, Q, C))