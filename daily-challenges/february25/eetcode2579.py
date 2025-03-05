"""
 # https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05
 # 2579. Count Total Number of Colored Cells
 # There exists an infinitely large two-dimensional grid of uncolored unit cells. 
 # You are given a positive integer n, indicating that you must do the following routine for n minutes:
   ## At the first minute, color any arbitrary unit cell blue.
   ## Every minute thereafter, color blue every uncolored cell that touches a blue cell.
 # Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.
"""
class leetcode2579:
    def __init__(self, name):
        self.name = name

    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """

        numBlueCells = 1

        """
        Method 1 : Using while 
        addend = 4 
        
        while n-1:
            numBlueCells += addend
            addend += 4
            n -= 1
        """

        for i in range(n):
            numBlueCells += 4*i

        return numBlueCells
