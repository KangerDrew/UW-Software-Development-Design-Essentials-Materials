import week5
def test_rpn_add():
  # arrange
  rpn = main.RPN()
  rpn.process(5)
  rpn.process(4)
  rpn.process("+")

  # act / assert
  assert rpn.result() == 9


def test_rpn_subtract():
  # arrange
  rpn = main.RPN()
  rpn.process(5)
  rpn.process(4)
  rpn.process("-")

  # act / assert
  assert rpn.result() == 1


def test_rpn_multiply():
  # arrange
  rpn = main.RPN()
  rpn.process(3)
  rpn.process(2)
  rpn.process("*")

  # act / assert
  assert rpn.result() == 6

def test_rpn_divide():
  # arrange
  rpn = main.RPN()
  rpn.process(9)
  rpn.process(3)
  rpn.process("/")

  # act / assert
  assert rpn.result() == 3

def test_rpn_all():
  # arrange
  rpn = main.RPN()
  rpn.process(5)
  rpn.process(4)
  rpn.process("+")
  rpn.process(3)
  rpn.process("/")
  rpn.process(5)
  rpn.process("*")
  rpn.process(15)
  rpn.process("-")

 # act / assert
  assert rpn.result() == 0

def test_remove_max():
  # arrange
  input = [7,77,88,2,97,5,117,107,61,107,52]
  # act / assert
  assert main.remove_max(input) == 117
  assert input == [7,77,88,2,97,5,107,61,107,52]
