from main import *
import pytest

def test_soma():
    result = soma(
        1,3
    )
    assert result == 4


def test_sub(payload):
    a = payload[0]
    b = payload[1]
    result = sub(a,b)

    assert result == -50


def test_multi_erro(payload_erro):
    a = payload_erro[0]
    b = payload_erro[1]
  
    with pytest.raises(Exception):
        multi(a,b)
