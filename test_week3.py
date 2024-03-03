import week3

def test_sum_three_numbers():
  assert main.sum([1, 3, 5]) == 9

def test_sum_five_numbers():
  assert main.sum([1, 3, 5, 13, 0]) == 22

def test_is_palindrome_no_spaces_negative():
  assert main.is_palindrome("enterprise") == False

def test_is_palindrome_no_spaces_positive():
  assert main.is_palindrome("racecar") == True

def test_is_palindrome_with_spaces_positive():
  assert main.is_palindrome("never odd or even") == True

def test_is_palindrome_with_spaces_negative():
 assert main.is_palindrome("not a palindrome") == False

def test_step_ways_zero():
  assert main.step_ways(0) == 1
  
def test_step_ways_four():
  assert main.step_ways(4) == 7

def test_step_ways_five():
  assert main.step_ways(5) == 13

def test_step_ways_fifteen():
  assert main.step_ways(15) == 5768

def test_step_ways_cached_hundred():
  assert main.step_ways_cached(100) == 180396380815100901214157639

def test_step_ways_cached_one_fifty():
  assert main.step_ways_cached(150) == 3081058855986474528462647721608166932600

def test_step_ways_cached_two_hundo():
  assert main.step_ways_cached(200) == 52622583840983769603765180599790256716084480555530641
