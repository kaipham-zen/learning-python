from Node import Node

import unittest


def assert_equal(got, expected, msg):
	"""
	Simple assert helper
	"""
	assert expected == got, \
		"[{}] Expected: {}, got: {}".format(msg, expected, got)


class SampleNodeTestCases(unittest.TestCase):
	"""
	Testing functionality of the Node class
	"""

	def setUp(self):
		"""
		Set up the tree to be used throughout the test
		This is the tree given in the sample
			 A(5)
		  /   |   \
		B(2) C(3) D(5)
		/
		E(9)
		"""
		k = 1
		self.A = Node(5, k)
		self.B = Node(2, k)
		self.C = Node(3, k)
		self.D = Node(5, k)
		self.E = Node(9, k)
		self.B.add_child(self.E)
		self.A.add_child(self.B)
		self.A.add_child(self.C)
		self.A.add_child(self.D)

	def test_is_external(self):
		"""
		Test that the sample tree has been correctly created
		"""
		assert_equal(self.A.is_external(), False, "A is not external")
		assert_equal(self.B.is_external(), False, "B is not external")
		assert_equal(self.C.is_external(), True, "C is external")
		assert_equal(self.D.is_external(), True, "D is external")
		assert_equal(self.E.is_external(), True, "E is external")

	def test_get_children(self):
		"""
		Test that the sample tree returns the correct child
		"""
		assert_equal(self.A.get_children(), [self.B, self.C, self.D], "A's children are [B, C, D]")
		assert_equal(self.B.get_children(), [self.E], "B's child is E")
		assert_equal(self.D.get_children(), [], "D has no children")
		assert_equal(self.C.get_children(), [], "C has no children")
		assert_equal(self.E.get_children(), [], "E has no children")

	def test_get_ksum(self):
		"""
		Test that the sample tree returns the correct gold and ksum
		"""
		nodes = [self.A, self.B, self.C, self.D, self.E]
		gold_values = [5,2,3,5,9]
		ksum = [9,9,3,5,9]
		for i in range(len(nodes)):
			u = nodes[i]
			assert_equal(u.gold, gold_values[i], "gold values "+str(i))
			assert_equal(u.k, 1, "k values "+str(i))
			assert_equal(u.return_k_sum(), ksum[i], "ksum values "+str(i))
			
	def test_update_gold(self):
		"""
		Test that the sample tree returns the correct gold and ksum after update_gold() is called
		"""
		nodes = [self.A, self.B, self.C, self.D, self.E]
		self.E.update_gold(10)
		gold_values = [5,2,3,5,10]
		ksum = [10,10,3,5,10]
		for i in range(len(nodes)):
			u = nodes[i]
			assert_equal(u.gold, gold_values[i], "gold values "+str(i))
			assert_equal(u.k, 1, "k values "+str(i))
			assert_equal(u.return_k_sum(), ksum[i], "ksum values "+str(i))

if __name__ == '__main__':
	unittest.main()