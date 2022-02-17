import unittest
import pytest
import math
from carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test againt
# this special case.

def test_get_age_carbon_14_dating():
    assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34, abs_tol=0.01)

def test_get_age_carbon_14_dating_nonpositive_input():
    assert math.isnan(get_age_carbon_14_dating(0))
    assert math.isnan(get_age_carbon_14_dating(-2.03))

    