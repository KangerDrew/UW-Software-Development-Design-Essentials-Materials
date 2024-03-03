import main

def test_merge():
  assert main.merge([5, 10, 15, 20], [3, 7, 13, 60, 100]) == [3, 5, 7, 10, 13, 15, 20, 60, 100]

def test_reverse_print(capsys):
  # arrange
  first = main.Node(1)
  first.next = main.Node(2)
  first.next.next = main.Node(3)

  # act
  main.reverse_print(first)

  # assert
  captured = capsys.readouterr()
  assert captured.out == "3\n2\n1\n"

def test_reverse():
  # arrange
  first = main.Node(1)
  first.next = main.Node(2)
  first.next.next = main.Node(3)

  # act
  actual = main.reverse(first)

  # assert
  assert actual is not None
  assert actual.data == 3
  assert actual.next is not None
  assert actual.next.data == 2
  assert actual.next.next is not None
  assert actual.next.next.data == 1
