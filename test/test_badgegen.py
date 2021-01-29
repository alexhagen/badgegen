"""Tests for badgegen Badge Generator."""
import badgegen
from svgpathtools import svg2paths

def test_init():
    """Test that the badge is initialized."""
    _badgegen = badgegen.BadgeGenerator()
    assert isinstance(_badgegen, badgegen.BadgeGenerator)

def test_gen_svg():
    """Test that the left rectangle is correct."""
    _badgegen = badgegen.BadgeGenerator()
    paths, attributes = svg2paths('badge.svg')
    assert(len(paths) == 2)
    assert(len(paths[0]) == 9)
    assert(attributes[0]['fill'] == '#000000')
    assert(attributes[1]['stroke'] == '#000000')

if __name__ == "__main__":
    test_init()
    test_gen_svg()