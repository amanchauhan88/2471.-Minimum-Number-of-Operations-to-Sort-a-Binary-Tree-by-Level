# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def min_swaps_to_sort(arr):
            # To find minimum swaps required to sort the array
            n = len(arr)
            arr_with_indices = [(val, idx) for idx, val in enumerate(arr)]
            arr_with_indices.sort()  # Sort by value
            
            visited = [False] * n
            swaps = 0
            
            for i in range(n):
                if visited[i] or arr_with_indices[i][1] == i:
                    continue
                
                # Count the size of the cycle
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = arr_with_indices[j][1]
                    cycle_size += 1
                
                # Add (cycle_size - 1) swaps
                if cycle_size > 1:
                    swaps += cycle_size - 1
            
            return swaps

        # Level order traversal to get values at each level
        levels = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current_level:
                levels.append(current_level)
        
        # Calculate minimum operations for each level
        min_operations = 0
        for level in levels:
            min_operations += min_swaps_to_sort(level)
        
        return min_operations
