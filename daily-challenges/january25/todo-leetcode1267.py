'''
   * 1267. Count servers that communicate
   * 
   * You are given a map of a server center, represented as a m * n integer matrix grid, 
   * where 1 means that on that cell there is a server and 0 means that it is no server. 
   * Two servers are said to communicate if they are on the same row or on the same column.
   * Return the number of servers that communicate with any other server.
 '''
class leetcode1267(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
