import pytest
import math
from geometry.cone import volume_cone

def test_volume_cone_valid_inputs():
    """
    Test volume computation for valid cone dimensions.
    """
    base_radius, height = 2.0, 6.5
    expected = 27.2271363
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)

def test_volume_cone_negative_dimension():
    """
    Document current behaviour when a negative dimension is used.
    """
    base_radius, height = 2.0, -6.5
    expected = -27.2271363
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)

def test_volume_cone_float_tolerance():
    """
    Test volume computation using approximate comparison.
    """
    base_radius, height = 2.1, 6.6
    expected = (1/3) * math.pi * base_radius**2 * height
    assert volume_cone(base_radius, height) == pytest.approx(expected, rel=1e-6)