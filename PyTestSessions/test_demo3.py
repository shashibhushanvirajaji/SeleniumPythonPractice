import pytest

def test_m12():
    assert True

@pytest.mark.asserting
def test_m22():
    assert 'bhushan' == 'bhushan'

def test_m902():
    assert False

def test_m41():
    assert 150 ==150

def test_m51():
    assert 550 != 150

@pytest.mark.logout
def testLogout():
    assert 'Logout'=='Logout'