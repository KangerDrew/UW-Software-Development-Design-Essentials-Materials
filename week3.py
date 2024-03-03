# 1. Write a method that takes in a list of integers and returns their sum
def sum(values):
  # Exit condition, if we get an empty array return 0:
  if not values:
    return 0
  
  # Remove a value from the values array (typically it is ideal to remove
  # from the end of the array because that is O(1) time complexity operation.
  # Python's list behaves bit differently than a traditional array, but .pop()
  # should still be a constant operation!):
  removed_val = values.pop()
  
  # Get the total sum by adding the popped value above, and calculating the remaining
  # array's sum by calling sum() function recursively on the remaining values in the list:
  total_sum = removed_val + sum(values)

  return total_sum
  
# 2. Write a method that determines if the passed string is a palindrome or not
def is_palindrome(string):
  # Exit condition, if we get an empty string, that means we've reached the
  # end of the recursion without returning False, or just got empty string as
  # an input. Either way that is technically a palindrome so return True:
  if not string:
    return True
  
  # Check the first and last character of the string. However, we need to check that
  # we selected a character, not an empty space. We'll use a pointer to get our 
  # character, and increment once or however many times as necessary until we find a
  # valid character:
  
  # ALSO make sure left & right pointers do not cross:

  left, right = 0, len(string) - 1

  while string[left] == " " and left < right:
    left += 1

  while string[right] == " " and left < right:
    right -= 1

  # Compare the characters at left & right pointer, and recursively do the same for the
  # inner strings without left and right character:
    
  # Sidenote: in python, when string slicing, the first index is inclusive, while the
  # last index is not. So the expression for next string without the first and last 
  # letter is string[left + 1:right]
  return string[left] == string[right] and is_palindrome(string[left + 1:right])
  

# 3. Implement a recursive method to count how many possible ways a child can 
#    run up n stairs 1 step, 2 steps, or 3 steps at a time.
def step_ways(steps):
  # Exit condition #1: If we reach exactly 0 step, it means we've found 1 valid
  # way to traverse up the stairs.
  if steps == 0:
    return 1
  
  # Exit condition #2: If we reach less than 0 step, it means we've over-stepped.
  # This is not a valid way to traverse up the stairs.
  if steps < 0:
    return 0
  
  # There are 3 possible ways a child could have reached the current step value.
  # To reach n steps, the child must have first climbed n - 1 steps, or n - 2 steps,
  # or n - 3 steps. We need to recursively determine how many ways a child can
  # climb those different steps. Adding those 3 results will give us the number of
  # ways the child can climb current steps!
  return step_ways(steps - 1) + step_ways(steps - 2) + step_ways(steps - 3)

  
# Challenge: Write a cached version of step_ways().
def step_ways_cached(steps, memo=None):

  # Python unique behavior. We can't set default mutable argument (memo={}). Instead,
  # we use if statement to set memo = {} when the function is called without memo argument
  if memo is None:
    memo = {}
  # Exit condition #0: If memo dictionary already contains solution to the current steps,
  # return that value:
  if steps in memo:
    return memo[steps]

  # Exit condition #1: If we reach exactly 0 step, it means we've found 1 valid
  # way to traverse up the stairs.
  if steps == 0:
    return 1
  
  # Exit condition #1: If we reach less than 0 step, it means we've over-stepped.
  # This is not a valid way to traverse up the stairs.
  if steps < 0:
    return 0
  
  # Store the number of ways to climb steps here, and return it:
  memo[steps] = step_ways_cached(steps - 1, memo) + step_ways_cached(steps - 2, memo) + step_ways_cached(steps - 3, memo)
  return memo[steps]
