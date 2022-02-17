import unittest
from unittest import mock
import pytest
import math
from calculate_grades import *

def test_calculate_stat():
    mean, std_dev = calculate_stat([90, 78, 45, 87, 94])
    assert math.isclose(mean, 78.8, abs_tol=0.01)
    assert math.isclose(std_dev, 19.79, abs_tol=0.01)
