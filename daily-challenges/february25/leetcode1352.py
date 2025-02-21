"""
 # https://leetcode.com/problems/product-of-the-last-k-numbers/?envType=daily-question&envId=2025-02-14
 # 1352. Product of the Last K Numbers
 # Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
 # Implement the ProductOfNumbers class:
   ## ProductOfNumbers() Initializes the object with an empty stream.
   ## void add(int num) Appends the integer num to the stream.
   ## int getProduct(int k) Returns the product of the last k numbers in the current list. 
   ## You can assume that always the current list has at least k numbers.
 # The test cases are generated so that, at any time, 
 # the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
"""
class leetcode1352(object):

    def __init__(self):        
        self.products = []
        self.current_product = 1
     
    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.products = []
            self.current_product = 1
        else:
            self.current_product *= num
            self.products.append(self.current_product)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k > len(self.products):
            return 0
        elif k == len(self.products):
            return self.current_product
        else:
            return self.current_product / self.products[len(self.products) - k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
