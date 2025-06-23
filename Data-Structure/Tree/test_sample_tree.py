from Node import Node
from Tree import Tree

import unittest


def assert_equal(got, expected, msg):
	"""
	Simple assert helper
	"""
	assert expected == got, \
		"[{}] Expected: {}, got: {}".format(msg, expected, got)


class SampleTreeTestCases(unittest.TestCase):
	"""
	Testing functionality of the Tree class
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
		self.tree = Tree(self.A)
		self.tree.put(self.B, self.E)
		self.tree.put(self.A, self.B)
		self.tree.put(self.A, self.C)
		self.tree.put(self.A, self.D)

	def test_construction(self):
		"""
		Test that the sample tree has been correctly constructed
		"""
		assert_equal(self.A.is_external(), False, "A is not external")
		assert_equal(self.B.is_external(), False, "B is not external")
		assert_equal(self.C.is_external(), True, "C is external")
		assert_equal(self.D.is_external(), True, "D is external")
		assert_equal(self.E.is_external(), True, "E is external")
		
		assert_equal(self.A.gold, 5, "A has gold of 5")
		assert_equal(self.B.gold, 2, "B has gold of 2")
		assert_equal(self.C.gold, 3, "C has gold of 3")
		assert_equal(self.D.gold, 5, "D has gold of 5")
		assert_equal(self.E.gold, 9, "E has gold of 9")
		
		assert_equal(self.A.return_k_sum(), 9, "A has a ksum of 9")
		assert_equal(self.B.return_k_sum(), 9, "B has a ksum of 9")
		assert_equal(self.C.return_k_sum(), 3, "C has a ksum of 3")
		assert_equal(self.D.return_k_sum(), 5, "D has a ksum of 5")
		assert_equal(self.E.return_k_sum(), 9, "E has a ksum of 9")

	def test_put(self):
		"""
		Test that the sample tree puts nodes correctly
		"""
		F = Node(12, 1)
		self.tree.put(self.C, F)

		"""
			A(5)
		  /   |   \
		B(2) C(3) D(5)
		/	  |
		E(9) F(12)
		"""
		assert_equal(self.A.is_external(), False, "A is not external")
		assert_equal(self.B.is_external(), False, "B is not external")
		assert_equal(self.C.is_external(), False, "C is not external")
		assert_equal(self.D.is_external(), True, "D is external")
		assert_equal(self.E.is_external(), True, "E is external")
		assert_equal(F.is_external(), True, "F is external")

		assert_equal(self.A.return_k_sum(), 12, "A has a ksum of 12")
		assert_equal(self.B.return_k_sum(), 9, "B has a ksum of 9")
		assert_equal(self.C.return_k_sum(), 12, "C has a ksum of 12")
		assert_equal(self.D.return_k_sum(), 5, "D has a ksum of 5")
		assert_equal(self.E.return_k_sum(), 9, "E has a ksum of 9")
		assert_equal(F.return_k_sum(), 12, "F has a ksum of 12")

	def test_move_subtree(self):
		"""
		Test that the sample tree moves subtree correctly
		"""
		self.tree.move_subtree(self.B, self.A)
		"""
			A(5)
		  /   |   \
		C(3) D(5) B(2) 
					\
					E(9)
		"""
		assert_equal(self.A.is_external(), False, "A is not external")
		assert_equal(self.B.is_external(), False, "B is not external")
		assert_equal(self.C.is_external(), True, "C is external")
		assert_equal(self.D.is_external(), True, "D is external")
		assert_equal(self.E.is_external(), True, "E is external")
		assert_equal(self.A.return_k_sum(), 9, "A has a ksum of 9")
		assert_equal(self.B.return_k_sum(), 9, "B has a ksum of 9")
		assert_equal(self.C.return_k_sum(), 3, "C has a ksum of 3")
		assert_equal(self.D.return_k_sum(), 5, "D has a ksum of 5")
		assert_equal(self.E.return_k_sum(), 9, "E has a ksum of 9")
		
		self.tree.move_subtree(self.B, self.D)
		assert_equal(self.D.is_external(), False, "D is not external")
		assert_equal(self.A.is_external(), False, "A is not external")
		assert_equal(self.B.is_external(), False, "B is not external")
		assert_equal(self.C.is_external(), True, "C is external")
		assert_equal(self.E.is_external(), True, "E is external")
		assert_equal(self.A.return_k_sum(), 9, "A has a ksum of 9")
		assert_equal(self.B.return_k_sum(), 9, "B has a ksum of 9")
		assert_equal(self.C.return_k_sum(), 3, "C has a ksum of 3")
		assert_equal(self.D.return_k_sum(), 9, "D has a ksum of 9")
		assert_equal(self.E.return_k_sum(), 9, "E has a ksum of 9")
		

	def test_melt(self):
		self.tree.melt_subtree(self.B)
		assert_equal(self.B.is_external(), True, "B is external")
		assert_equal(self.B.gold, 11, "B has 11 gold (9+2)")
		assert_equal(self.A.gold, 5, "A has 5 gold")
		assert_equal(self.C.gold, 3, "C has 3 gold")
		assert_equal(self.D.gold, 5, "D has 5 gold")
		assert_equal(self.A.return_k_sum(), 11, "A has a ksum of 11")
		assert_equal(self.B.return_k_sum(), 11, "B has a ksum of 11")
		assert_equal(self.C.return_k_sum(), 3, "C has a ksum of 3")
		assert_equal(self.D.return_k_sum(), 5, "D has a ksum of 5")
		
if __name__ == '__main__':
	unittest.main()