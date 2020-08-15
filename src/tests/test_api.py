import pytest, sys, os, requests

top_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(top_dir)
from config.settings import getConfig

#@pytest.mark.test
def test_correctly():
    a = -1
    assert a < 0
