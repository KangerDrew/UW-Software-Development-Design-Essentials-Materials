import hashHelpers


def test_hashFunc():
    assert hashHelpers.hashFunc("DanceDance") == 184017123273315024
    assert hashHelpers.hashFunc("ThnksfrthMmrs") == 95841068531666107686316
    assert hashHelpers.hashFunc("TheTakeOvertheBreaksOver") == 4986834331548489546378644545877396790229673

def test_hash2Index():
    assert hashHelpers.hash2Index(9, 10) == 9
    assert hashHelpers.hash2Index(4, 3) == 1
    assert hashHelpers.hash2Index(20, 10) == 0

