from HashMapChaining import HashMapChaining
import pytest


def test_hmc_set_value():

    test_hash = HashMapChaining()
    test_hash.setValue("0", 23)

    assert test_hash.table[0].value == 23


def test_hmc_set_value_chaining():

    test_hash = HashMapChaining()
    test_hash.setValue("0", 23)
    test_hash.setValue("A", 64)

    assert test_hash.table[0].next.value == 64


def test_hmc_set_value_override():

    test_hash = HashMapChaining()
    test_hash.setValue("0", 23)
    test_hash.setValue("0", 32)

    assert test_hash.table[0].value == 32
    assert test_hash.node_count == 1


def test_hmc_get_value():

    test_hash = HashMapChaining()
    test_hash.setValue("0", 23)

    assert test_hash.getValue("0") == 23


def test_hmc_get_value_chaining():

    test_hash = HashMapChaining()
    test_hash.setValue("0", 23)
    test_hash.setValue("A", 64)

    assert test_hash.getValue("A") == 64


def test_hmc_get_value_error():

    test_hash = HashMapChaining()
    test_hash.setValue("0", 23)

    with pytest.raises(KeyError) as err1:
        test_hash.getValue("notindic")

    assert err1.value.args[0] == "notindic"

    # Also test that KeyError statement gets raised after
    # traversing the linked list.
    with pytest.raises(KeyError) as err2:
        test_hash.getValue("A")

    assert err2.value.args[0] == "A"


def test_hmc_rehash():

    test_hash = HashMapChaining()
    test_hash.setValue("0", 0)
    test_hash.setValue("1", 1)
    test_hash.setValue("2", 2)
    test_hash.setValue("3", 3)
    test_hash.setValue("4", 4)
    test_hash.setValue("5", 5)
    test_hash.setValue("6", 6)
    test_hash.setValue("7", 7)
    test_hash.setValue("8", 8)
    test_hash.setValue("9", 9)
    test_hash.setValue("A", 10)
    test_hash.setValue("B", 11)
    test_hash.setValue("C", 12)
    test_hash.setValue("D", 13)
    test_hash.setValue("E", 14)

    assert test_hash.table_len == 10

    test_hash.setValue("F", 15)

    assert test_hash.table_len == 20
