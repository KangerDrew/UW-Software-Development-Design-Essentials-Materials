import week6

def test_in_order():
  #arrange
  tree = main.Tree([10, 15, 7, 9, 3, 24, 36])

  #act / assert
  assert tree.in_order() == "3 7 9 10 15 24 36" 

def test_pre_order():
  #arrange
  tree = main.Tree([10, 15, 7, 9, 3, 24, 36])

  #act / assert
  assert tree.pre_order() == "10 7 3 9 15 24 36"

def test_post_order():
  #arrange
  tree = main.Tree([10, 15, 7, 9, 3, 24, 36])

  #act / assert
  assert tree.post_order() == "3 9 7 36 24 15 10" 
  
def test_height():
  #arrange
  tree = main.Tree([10, 15, 7, 9, 3, 24, 36])

  #act / assert
  assert tree.height() == 3

def test_sum():
  #arrange
  tree = main.Tree([10, 15, 7, 9, 3, 24, 36])

  #act / assert
  assert tree.sum() == 104

def test_contains():
  #arrange
  tree = main.Tree([10, 15, 7, 9, 3, 24, 36])

  #act / assert
  assert tree.contains(7) == True 
