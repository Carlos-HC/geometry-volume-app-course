import pytest
import math
from geometry.sphere import volume_sphere

def test_volume_sphere_valid_inputs():
    """
    Test volume computation for valid cone dimensions.
    """
    radius = 2.0
    expected = 33.5103216
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)

def test_volume_sphere_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    radius = -2.0
    expected = -33.5103216
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)

def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    radius = 2.0
    expected = (4 / 3) * math.pi * radius ** 3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)