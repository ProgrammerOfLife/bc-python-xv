import unittest 
from two_sum import two_sum

class TwoSumTestSuit(unittest.TestCase):
	def test_list_range_4(self):
		res = two_sum([2,5,1,7], 8)
		self.assertEqual(res,[2,3])

	def test_list_range_5(self):
		res = two_sum([2,3,4,5,6], 9)
		self.assertEqual(res,[1,4])


	def test_list_range_6(self):
		res = two_sum([1,2,3,4,5,6], 11)
		self.assertEqual(res, [4,5])

	def test_list_range_7(self):
		res = two_sum([2,5,1,7,6,3,8], 15)
		self.assertEqual(res,[3,6])

	def test_list_range_8(self):
		res = two_sum([2,5,1,7,6,3,8,10], 18)
		self.assertEqual(res,[6,7])

	def test_list_range_9(self):
		res = two_sum([5,4,23,7,2,9,11,6,8], 25)
		self.assertEqual(res,[2,4])

	def test_list_range_10(self):
		res = two_sum([2,5,1,7,6,3,8,54,12,9], 19)
		self.assertEqual(res,[3,8])

	def test_list_range_11(self):
		res = two_sum([13,4,6,8,9,12,15,25,78,23,5], 38)
		self.assertEqual(res,[0,7])

	def test_list_range_12(self):
		res = two_sum([2,5,1,7,6,3,8,54,12,9,15,30], 42)
		self.assertEqual(res,[8,11])	

	def test_list_range_13(self):
		res = two_sum([12,4,67,8,5,23,55,16,9,11,2,50,78], 105)
		self.assertEqual(res,[6,11])

	def test_list_range_14(self):
		res = two_sum([2,5,1,7,6,3,8,54,12,9,78,45,32,90], 144)
		self.assertEqual(res,[7,13])


if __name__ == "__main__":
	unittest.main()