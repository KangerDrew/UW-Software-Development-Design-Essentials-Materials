from HashMapLinearProbing import HashMapLinearProbing
import pytest


def test_hmlp_set_value():

    test_hash = HashMapLinearProbing()
    test_hash.setValue("0", 23)

    # Second element of the tuple in the table should be the value:
    assert test_hash.table[0][1] == 23


def test_hmlp_set_value_linear_probing():

    test_hash = HashMapLinearProbing()
    test_hash.setValue("0", 23)
    test_hash.setValue("A", 64)

    assert test_hash.table[1][1] == 64


def test_hmlp_set_value_override():

    test_hash = HashMapLinearProbing()
    test_hash.setValue("0", 23)
    test_hash.setValue("0", 64)

    assert test_hash.table[0][1] == 64


def test_hmlp_get_value():

    test_hash = HashMapLinearProbing()
    test_hash.setValue("0", 23)

    assert test_hash.getValue("0") == 23


def test_hmlp_get_value_chaining():

    test_hash = HashMapLinearProbing()
    test_hash.setValue("0", 23)
    test_hash.setValue("A", 64)

    assert test_hash.getValue("A") == 64


def test_hmlp_get_value_error():

    test_hash = HashMapLinearProbing()
    test_hash.setValue("0", 23)

    with pytest.raises(KeyError) as err1:
        test_hash.getValue("notindic")

    assert err1.value.args[0] == "notindic"


def test_hmc_rehash():

    test_hash = HashMapLinearProbing()
    test_hash.setValue("0", 0)
    test_hash.setValue("1", 1)
    test_hash.setValue("2", 2)
    test_hash.setValue("3", 3)
    test_hash.setValue("4", 4)
    test_hash.setValue("5", 5)
    test_hash.setValue("6", 6)

    assert test_hash.table_len == 10

    test_hash.setValue("7", 7)

    assert test_hash.table_len == 20
