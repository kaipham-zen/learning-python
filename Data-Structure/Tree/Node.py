"""
Tree Node
----------

This class represents an individual Node in a Tree. 

Each Node consists of the following properties:
	- children: List of child Nodes
	- parent: Pointer to the parent Node in the tree
	- gold: The gold at this point
	- k_sum: The sum of the k highest gold values in the subtree rooted at this node

The class also supports the following functions:
	- add_child(Node): Adds the given Node as a child
	- is_external(): Returns True if the Node is a leaf node
	- get_children(): Returns the children of this node
	- update_gold(int): Updates the gold value at this node to the given value
	- return_k_sum(): Returns the k_sum at this node
"""


class Node():
	# These are the defined properties as described above
	children: list['Node']
	parent: 'Node'
	gold: int
	k_sum: int
	k: int
	sub_sum: int
	subtree_gold: list
	
	def __init__(self, gold: int, k: int) -> None:
		"""
		The constructor for the Node class.
		:param gold: The gold of the node.
		:param k: Value used to calculate k_sum.
		"""
		self.gold = gold
		self.k = k
		self.k_sum = 0
		self.sub_sum = gold
		self.subtree_gold = [gold]
		self.children = []
		self.parent = None

	def add_child(self, node: 'Node') -> None:
		"""
		Adds the given node as a child of the current node.
		The given node is guaranteed to be new and not a child of any other node.
		:param node: The node to add as the child
		"""
		self.children.append(node)
		node.parent = self
		self.k_sum = self.return_k_sum()

	def is_external(self) -> bool:
		"""
		Returns True if the node is a leaf node.
		:return: True if the node is a leaf node.
		"""
		return len(self.children) == 0

	def update_gold(self, gold: int) -> None:
		"""
		Updates the gold of the current node.
		:param gold: The new gold of the node.
		"""
		self.gold = gold
		self.k_sum = self.return_k_sum()

	def get_children(self) -> list['Node']:
		"""
		Returns the children of the current node.
		:return: The children of the current node.
		"""
		return self.children

	def get_all_sub_nodes(self) -> None:
		self.subtree_gold = [self.gold]
		for child in self.children:
			child.get_all_sub_nodes()
			self.subtree_gold += child.subtree_gold

	def return_k_sum(self) -> int:
		"""
		Returns the k_sum of the current node.
		:return: The k_sum of the current node.
		"""
		if self.is_external():
			self.k_sum = self.gold
		else:
			self.get_all_sub_nodes()
			self.k_sum = 0
			if len(self.subtree_gold) <= self.k:
				self.k_sum = sum(self.subtree_gold)
			else:
				self.subtree_gold.sort(reverse=True)
				for i in range(self.k):
					self.k_sum += self.subtree_gold[i]

		return self.k_sum
		
	def parental_recursive_ksum(self) -> None:
		if self.parent is not None:
			self.parent.k_sum = self.parent.return_k_sum()


