from collections import deque

# 1. Create a Reverse Polish Notation calculator
class RPN:

  # Constructor: when RPN is initialized, we'll need a stack to keep track of
  # all the values:
  def __init__(self) -> None:
    self.stack = []

  def process(self, value):
    # If value is not an integer (assuming we're only getting integer for our
    # numerical input), that means we have an operator:
    if not isinstance(value, int):
      # Get two values stored within stack:
      stack_val_2 = self.stack.pop()
      stack_val_1 = self.stack.pop()

      # Perform the specified operator from value input:
      match value:
        case "+":
          self.stack.append(stack_val_1 + stack_val_2)
        case "-":
          self.stack.append(stack_val_1 - stack_val_2)
        case "*":
          self.stack.append(stack_val_1 * stack_val_2)
        case "/":
          self.stack.append(stack_val_1 / stack_val_2)
      
      # return None to exit out of function (stylistic choice. 
      # I don't use else statement unless I have to)
      return None
    
    # If the above if statement didn't trigger, it means we have numeric input.
    # Store it inside the stack:
    self.stack.append(value)
    return None
  
  def result(self):
    # Peek the top of the stack and return the value:
    return self.stack[-1]


# 2. Write a method that removes the maximum value from a stack
def remove_max(values):
  
  # Assuming the stack is not ordered, we'll have to remove each item from stack
  # one by one to assess which value is greatest...

  # Initialize a temporary queue where we will store the values:
  temp_queue = deque([])
  # Initialize an int variable that'll keep track of the max value in the original stack:
  max_val = 0

  while values:
    # Remove from top of the stack:
    current = values.pop()    
    # Use max() python function to set the new max_val value:
    max_val = max(max_val, current)
    # Append the current into the temp_queue:
    temp_queue.append(current)

  # Once all the values are in queue, the order be flipped compared to the original stack.
  # Add them back excpet for the max value:
  while temp_queue:
    current = temp_queue.popleft()
    if current != max_val:
      values.append(current)

  # At this time, our stack is flipped (because we used queue to store our values)
  # Remove everything from stack to queue again, and then back to stack so that the
  # values are in correct order again!
  while values:
    temp_queue.append(values.pop())
  while temp_queue:
    values.append(temp_queue.popleft())

  # Return the removed max val:  
  return max_val
