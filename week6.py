class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Tree:
  # 1) Write a function that takes in a list of integers, creates a binary tree with those integers
  def __init__(self, values):

    # Create the head of the tree using the first element in the values list. If an empty
    # list is provided, set head to null:
    self.head = TreeNode(values[0]) if values else None

    # Loop through the remaining values (if there are any), and 
    # add them to the tree using BST logic:
    for val_to_insert in values[1:]:
      
      current = self.head

      while current:
        if val_to_insert > current.value:
          
          if not current.right:
            current.right = TreeNode(val_to_insert)
            break
          else:
            current = current.right

        else:
          
          if not current.left:
            current.left = TreeNode(val_to_insert)
            break
          else:
            current = current.left
  
  # 2) Write a function that returns the in-order traversal of the tree as space-separated string.
  def in_order(self):
    order = []

    def dfs_inorder(node):
      if not node:
        return None
      
      dfs_inorder(node.left)
      order.append(node.value)
      dfs_inorder(node.right)

    dfs_inorder(self.head)
    return " ".join(str(x) for x in order)
  
  # 3) Write a function that returns the pre-order traversal of the tree as space-separated string.
  def pre_order(self):

    order = []

    def dfs_preorder(node):
      if not node:
        return None

      order.append(node.value)
      dfs_preorder(node.left)
      dfs_preorder(node.right)

    dfs_preorder(self.head)
    return " ".join(str(x) for x in order)
  
  # 4) Write a function that returns the post-order traversal of the tree as space-separated string.
  def post_order(self):
    order = []

    def dfs_postorder(node):
      if not node:
        return None

      dfs_postorder(node.left)
      dfs_postorder(node.right)
      order.append(node.value)

    dfs_postorder(self.head)
    return " ".join(str(x) for x in order)
  
  # 5) Write a function that determines the height of a given tree.
  def height(self):
    
    def dfs_height(node, depth):
      if not node:
        return depth - 1
      
      depth += 1

      left_height = dfs_height(node.left, depth)
      rigth_height = dfs_height(node.right, depth)

      return left_height if left_height > rigth_height else rigth_height
    
    return dfs_height(self.head, 0)


  
  # 6) Write a function that returns the sum of all values in a tree.
  def sum(self):
    total = 0

    def dfs_sum(node):
      if not node:
        return None
      
      nonlocal total
      total += node.value
      dfs_sum(node.left)
      dfs_sum(node.right)
      return None
    
    dfs_sum(self.head)
    return total
      
  
  # 7) Write a function that returns a bool indicating that a value exists (or not) in a given tree.
  def contains(self, value):
    
    def dfs_scan(node):
      if not node:
        return False
      
      if value == node.value:
        return True
      
      return dfs_scan(node.left) or dfs_scan(node.right)
    
    return dfs_scan(self.head)

# Extra Problems:
# 1) Implement node deletion from your tree. 
# 2) Write a function that flips a binary tree (any binary tree).
# 3) Given both a pre-order and in-order traversal of a tree, can you
# work backwards and recreate the exact structure that produced those traversals?
# Describe how that could be done, or if it's not possible, why it's not.





