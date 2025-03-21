# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c5Q9FUwcxmndv0zCrNhQfP6x1Xg0mGFC
"""

import collections
def bfs(graph, root):
  visited, queue = set(), collections.deque([root])
  visited.add(root)
  while queue:
    vertex = queue.popleft()
    print(str(vertex)+" ", end="")
    for neighbour in graph[vertex]:
      if neighbour not in visited:
        visited.add(neighbour)
        queue.append(neighbour)
if __name__ == '__main__':
  graph = {0:[1,2], 1:[2], 2:[3],3:[1,2]}
  print("following is breadth first traversal")
  bfs(graph, 0)