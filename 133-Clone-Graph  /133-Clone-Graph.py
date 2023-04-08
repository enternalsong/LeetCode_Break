"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        queue = [node]
        clone_node = Node(node.val)
        visited[node] = clone_node
        
        while queue:
            cur_node = queue.pop(0)
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[cur_node].neighbors.append(visited[neighbor])
        
        return clone_node