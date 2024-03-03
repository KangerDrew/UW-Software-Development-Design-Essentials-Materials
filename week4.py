from collections import deque

def merge(a, b):
  # Convert array a and b into doubly ended queue (Allows the use of .popleft(), which has
  # O(1) time complexity, unlike standard python list's .pop(0), which has O(n) complexity!)

  a, b = deque(a), deque(b)

  # Define a list/array that will contain the final result:
  final_arr = deque([])

  # Use while loop, where we continue looping until one of the array runs out integers:
  while a and b:
    if a[0] > b[0]:
      final_arr.append(b.popleft())
    else:
      final_arr.append(a.popleft())
  
  # If there are any integers left within a, append the rest to the final_arr
  if a:
    final_arr = final_arr + a

  # Do the same for b (only one of the if statement will trigger):
  if b:
    final_arr = final_arr + b

  # Return the final_arr (convert back to python list so the test passes):
  return list(final_arr)

class Node:
  def __init__(self, data=None, next=None):
      self.data = data
      self.next = next


def reverse_print(x: Node) -> None:
  # Exit condition. When we finish traversing the LinkedList,
  # Remove stack.
  if not x:
    return None

  # In recursive stack, the print statement will not trigger until
  # we reach the end of the stack. As per "Last in First Out" principle,
  # the recursive stack that's on the top (i.e. the function that's analyzing 
  # the node closest to the end of the linked list) will evaluate first:
  reverse_print(x.next)
  print(x.data)
  return None


def reverse(x: Node) -> Node: 
  # Define 3 pointers. 
  # Pointer 1 will stay behind the "current node" [prev]
  # Pointer 2 will be at the middle, where we will swap the pointer [current]
  # Pointer 3 will be ahead of the "current node" [after]
  prev = None
  current = x
  after = x.next

  # Use while loop to increment the pointers. We reverse the pointer at the center,
  # where the order needs to be swapped. Then, we change the reference of the pointers
  # so that we are positioned at the next node where the pointer needs to be changed.
  while after:
    
    current.next = prev
    prev = current
    current = after
    after = after.next

  # If the while loop above finished executing, "current" should be at the last node
  # of the linked list. However, due to the exit condition, it is still pointing at
  # null reference. We should have access to the 2nd last node via "prev", so switch
  # the pointer one last time, and return the "current" - a.k.a. the last node of the
  # original linked list, a.k.a. new head of the reversed linked list!.
  current.next = prev
  return current
