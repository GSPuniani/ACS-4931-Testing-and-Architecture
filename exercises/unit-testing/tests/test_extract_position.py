import pytest
from extract_position import extract_position

def test_extract_position():
    assert float(extract_position('|update| the positron location in the particle accelerator is x:-18.739')) == -18.739

def test_extract_position_none():
    assert extract_position(0) == None
    assert extract_position('|debug| ValueError') == None
    assert extract_position('|error| the positron location cannot be determined') == None
    assert extract_position('E') == None
