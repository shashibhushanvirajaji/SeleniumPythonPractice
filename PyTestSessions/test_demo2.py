import pytest

def testm132():
    assert True

@pytest.mark.asserting
def test_m322():
    assert 'reddy' == 'reddy'

def test_m28():
    assert False

def test_m44():
    assert 150 ==150

def test_m56():
    assert 550 != 150

@pytest.mark.logout
def testLogout():
    assert 'Logout'=='Logout'