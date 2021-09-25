# Heaps

A heap is a data structure that satisfies a heap property. A heap property states that there must be a certain
relationship between a parent node and its child nodes. This property must apply throughout the entire heap.

### Min heap

In a min heap, the relationship between parent and children is that the value at the parent must always be less than or
equal to its children. As a consequence of this, the lowest element in the heap must be the root node.

### Max heap

In a max heap, on the other hand, the parent is greater than or equal to its child or its children. It follows from this
that the largest value makes up the root node.

The heaps are binary trees, and although we are going to use a binary tree, we will actually use a list to represent it.
The heap stores a complete binary tree. To make the math with indexes easier, we are going to leave the first item in
the list (index 0) empty. After that, we place the tree nodes into the list, from top to bottom and left to right

You can retrieve the children of any node at the n index very easily. The left child is located at 2n, and the right
child is located at *2n + 1*. This will always hold true.For example, the C node would be at the 3 index, as C is a right
child of the A node, whose index is 1, so it becomes *2n+1 = 2 * 1 + 1 = 3*.