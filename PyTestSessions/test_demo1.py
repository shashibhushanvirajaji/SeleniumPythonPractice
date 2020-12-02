import pytest

def testm51():
    assert True

@pytest.mark.asserting
def test_m25():
    assert 'shashi' == 'shashi'

def test_m53():
    assert False

def test_m45():
    assert 150 ==150

def test_m57():
    assert 550 != 150

@pytest.mark.logout
def testLogout():
    assert 'Logout'=='logout'