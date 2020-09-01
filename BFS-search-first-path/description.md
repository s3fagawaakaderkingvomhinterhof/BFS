# BFS for get first path

Input: Is a directed graph as adjacency matrix.
Output: Is a path consisting of the nodes from start to destination. 

In this implementation the first found path is returned or None if no path is found.
All other paths are not important.

Idea: To avoid returning None the last statement of the BFS could be return [-1, -1]. Then you can check for this path and know that it is not valid.
