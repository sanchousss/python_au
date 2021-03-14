# Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)

## Maximum Depth of Binary Tree

<https://leetcode.com/problems/maximum-depth-of-binary-tree/>

``` python
def maxDepth(self, root: TreeNode) -> int:
    if not root:
      return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

```

## Binary Tree Inorder Traversal

<https://leetcode.com/problems/binary-tree-inorder-traversal/>

``` python
def inorderTraversal(self, root: TreeNode) -> List[int]:
    ans = []
    stack = []

    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      ans.append(root.val)
      root = root.right

    return ans
```

## Invert Binary Tree

<https://leetcode.com/problems/invert-binary-tree/>

``` python
def invertTree(self, root):
    
    if root is None:
        return None
    
    root.left, root.right = \
        self.invertTree(root.right), self.invertTree(root.left)
    
    return root
```

## Binary Search Tree Iterator

<https://leetcode.com/problems/binary-search-tree-iterator/>

``` python
def __init__(self, root: TreeNode):
    self.stack = []
    self.pushLeftsUntilNone(root)

  def next(self) -> int:
    root = self.stack.pop()
    self.pushLeftsUntilNone(root.right)
    return root.val

  def hasNext(self) -> bool:
    return self.stack

  def pushLeftsUntilNone(self, root: TreeNode):
    while root:
      self.stack.append(root)
      root = root.left
```

## Binary Tree Level Order Traversal

<https://leetcode.com/problems/binary-tree-level-order-traversal/>

``` python
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []

    ans = []
    queue = deque([root])

    while queue:
      currLevel = []
      for _ in range(len(queue)):
        node = queue.popleft()
        currLevel.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      ans.append(currLevel)

    return ans
```

## Kth Smallest Element in a BST

<https://leetcode.com/problems/kth-smallest-element-in-a-bst/>

``` python
def kthSmallest(self, root: TreeNode, k: int) -> int:
    def inorder(root: TreeNode) -> List[TreeNode]:
      if not root:
        return []

      return inorder(root.left) + [root.val] + inorder(root.right)

    return inorder(root)[k - 1]
```

## Validate Binary Search Tree

<https://leetcode.com/problems/validate-binary-search-tree/>

``` python
def isValidBST(self, root: TreeNode) -> bool:
    def isValidBST(root, minNode, maxNode):
      if not root:
        return True
      if minNode and root.val <= minNode.val:
        return False
      if maxNode and root.val >= maxNode.val:
        return False

      return isValidBST(root.left, minNode, root) and \
          isValidBST(root.right, root, maxNode)

    return isValidBST(root, None, None)
```

## Symmetric Tree

<https://leetcode.com/problems/symmetric-tree/>

``` python
def isSymmetric(self, root: TreeNode) -> bool:
    def isSymmetric(p: TreeNode, q: TreeNode) -> bool:
      if not p or not q:
        return p == q

      return p.val == q.val and \
          isSymmetric(p.left, q.right) and \
          isSymmetric(p.right, q.left)

    return isSymmetric(root, root)
```
