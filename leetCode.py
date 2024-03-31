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

class ListNode:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

head = ListNode(0)
listNode2 = ListNode(1)
listNode3 = ListNode(2)
listNode4 = ListNode(3)
listNode5 = ListNode(4)
listNode6 = ListNode(5)

head.next = listNode2
listNode2.next = listNode3
listNode3.next = listNode4
listNode4.next = listNode5
listNode5.next = listNode6


def sumList(head):
    if not head:
        return 0
    return(head.value + sumList(head.next))

print(sumList(head))


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


# def getleafs(root,leafs):
#     if not root:
#         return
#     if not root.left and not root.right:
#         leafs.append(root.value)
#         return
#     getleafs(root.left,leafs)
#     getleafs(root.right,leafs)

#     return leafs

# print(getleafs(root,[]))


# def reverseString (s):
#     res = ''
#     length = len(s)-1
#     while length >= 0:
#         res = res+s[length]
#         length-=1
#     return res

# print(reverseString('jalal'))

    
    

