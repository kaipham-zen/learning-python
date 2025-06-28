This is part of the assignment at USYD 2024S2 in Data Structure and Algorithm unit

# Story
Dwarves love digging for treasure and our lovely dwarves at the Moria Gold Digging Company of Middle-Earth are no exception. In fact, they have perfected their method of mining gold: they dig a straight line until they find gold and only at locations where they previously found this precious metal they branch out to search in different directions. To maintain the stability of their mining operation and avoid collapsing tunnels, they take extra care to ensure that none of their tunnels links up with any existing ones. In other words, their mining tunnels form a tree.

The administrative section of the Moria Gold Digging Company has hired you to assist them with keeping track of what tunnels exist and how much gold can be found at each location. As the dwarves mine gold from existing locations and look around, the available gold at each location may need to be updated.

To allow for efficient retrieval of the most prosperous locations of gold, you’re asked to maintain for each node of the tree the sum of the k highest amounts of gold in the subtree rooted at that node. Note that k is given to you at construction time and won’t change during the execution, but you can’t assume anything about the value of k itself; it can be anything between 1 and n (the number of nodes in the tree).

Unfortunately for the dwarves, the land of Middle-Earth isn’t exactly stable. Because of this, occasionally the tunnels move, changing the edges within our tree. After extensive research, the dwarves discovered that their tunnels always form a tree, even after the tunnels are changed, but which gold locations are connected can change.

And finally, dwarves do sometimes dig too deep… This causes lava from the core of Middle-Earth to engulf their tunnels, destroying them in the process. The extreme heat, however, also melts all the gold and deposits it at the root of the engulfed subtree. Our data structure should be able to handle these changes as well.

Informally, our implementation should support the following operations:

Update the amount of gold available at a node.

Insert a new node, connecting it to an existing one. This helps to keep track of the newly dug tunnels.

Return the summed value of the k highest amounts of gold in the subtree of a given node.

Move the subtree rooted at a given node. This models the changing tunnels of Middle-Earth.

Keep track of the effects of lava by removing subtrees and updating the amount of gold stored.

All operations need to maintain that every node correctly stores the sum of the k highest gold locations in its subtree.

# Task
Maintain a tree where each node in the tree holds a gold value as its key, as well as the property k_sum. The value of the "k_sum" is equivalent to the summed gold value of the k highest gold values in the subtree of the node.

## Move Subtree

You must also support the move_subtree(node_a, node_b) function, where the subtree rooted at node_a is made into a child of node_b. If node_b already has children, your function should make node_a the last child. You must ensure that the k_sum property is correct for all nodes, after moving the subtree. You can assume that node_b isn’t in the subtree of node_a and you don’t have to check for this.

## Melt Subtree

Your tree must support the melt_subtree(node_a) operation. When called, the function removes the subtree rooted at node_a and update the gold value of node_a with the sum of the gold in its (removed) subtree. You must ensure that the k_sum property is correct for all nodes, after moving the subtree.

You should strive to make your implementation as efficient as possible. Note that while we don’t explicitly test for the efficiency of your implementation, using inefficient implementations may cause timeouts.

## Testing
There are some test cases in this repository. We will be using unit tests provided with the unittest package of python.

## Running Tests

From the base directory (the one with node.py and tree.py), run

python -m unittest -v test_sample_tree.py test_sample_node.py
Or, running all the tests by:

python -m unittest -vv
