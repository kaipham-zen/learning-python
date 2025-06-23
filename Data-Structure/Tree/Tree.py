from Node import Node

"""
Tree
----------

This class represents the Tree used to model our dwarven mine. 

Each Tree consists of the following properties:
	- root: The root of the Tree

The class also supports the following functions:
	- put(node_a, node_b): Adds node_b as the last child of node_a
	- move_subtree(node_a, node_b): Move node_a to the last child of node_b. Update k_sum
	- melt_subtree(node): Removes the subtree of the node and updates the node's gold with the sum of the gold in its subtree. Update k_sum
"""


class Tree():
	# These are the defined properties as described above
	root: Node

	def __init__(self, root: Node = None) -> None:
		"""
		The constructor for the Tree class.
		:param root: The root node of the Tree.
		"""
		self.root = root

	def put(self, node_a: Node, node_b: Node) -> None:
		"""
		Adds node_b as the last child of node_a.
		You are guranteed that the given node is not already part of the tree
		:param node_a: The node to add the child to.
		:param node_b: The child to add to the node.
		"""
		node_a.add_child(node_b)

	def move_subtree(self, node_a: Node, node_b: Node) -> None:
		"""
		The subtree rooted at node_a is made into a child of node_b. 
		If node_b already has children, your function should make node_a the last child. 
		You must ensure that the k_sum property is correct for all nodes, after moving the subtree. 
		You can assume that node_b isn't in the subtree of node_a and you don't have to check for this.
		:param node_a: The root of the subtree to move.
		:param node_b: The node to add the subtree to.
		"""
		node_a.parent.children.remove(node_a)
		parent_node = node_a.parent
		node_b.add_child(node_a)
		parent_node.return_k_sum()
		node_a.return_k_sum()
		node_a.parental_recursive_ksum()

	def melt_subtree(self, node_a) -> None:
		"""
		Removes the subtree rooted at node_a and updates the gold value of node_a with the sum of the gold in its (removed) subtree. 
		You must ensure that the k_sum property is correct for all nodes, after removing the subtree and updating the gold value.
		"""
		node_a.get_all_sub_nodes()
		node_a.sub_sum = sum(node_a.subtree_gold)
		node_a.gold = node_a.sub_sum
		node_a.return_k_sum()
		node_a.parental_recursive_ksum()
		node_a.children=[]
		

		