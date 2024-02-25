import main

def test_decode():
    assert main.to_base_10("LpuPe81bc2w") == 18327995462734721974

def test_encode():
    assert main.to_base_62(18327995462734721974) == "LpuPe81bc2w"
