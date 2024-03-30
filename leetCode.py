import collections

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

root.left = node2
root.right = node3
node3.left = node4
node3.right = node5


# def bfs (root):
#     res =[]
#     q = collections.deque()
#     q.append(root)
#     while q:
#         level = []
#         qlen = len(q)
#         for i in range(qlen):
#             node = q.popleft()
#             if node:
#                 level.append(node.value)
#                 q.append(node.left)
#                 q.append(node.right)
#         if level:
#             res.append(level)
#     return res
  

# print(bfs(root))

# def dfs(root):
#     if not root:
#         return 0
#     return (1 +max(dfs(root.left),dfs(root.right)))

# print(dfs(root))

# def dfsWithoutRecursion(root):
#     res = 0
#     stack = [[root,1]]
#     while stack:
#         node,depth = stack.pop()
#         if node:
#             res = max(res,depth)
#             stack.append([node.left,depth+1])
#             stack.append([node.right,depth+1])
#     return res

# print(dfsWithoutRecursion(root))

# def bfs(root):
#     res = []
#     q = collections.deque()
#     q.append(root)
#     while q:
#         level =[]
#         qlen = len(q)
#         for i in range(qlen):
#             node = q.popleft()
#             if(node):
#                 level.append(node.value)
#                 q.append(node.left)
#                 q.append(node.right)
#         if level:
#             res.append(level)
#     return res

# # print(bfs(root))


# def dfs(root):
#     if  not root:
#         return 0
#     return(1+max(dfs(root.left),dfs(root.right)))

# print(dfs(root))


def getleafs(root,leafs):
    if not root:
        return
    if not root.left and not root.right:
        leafs.append(root.value)
        return
    getleafs(root.left,leafs)
    getleafs(root.right,leafs)

    return leafs

print(getleafs(root,[]))
    
    

