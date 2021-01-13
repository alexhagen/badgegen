import argparse
import svgwrite
from svgwrite.shapes import Line

class BadgeGenerator:
    def __init__(self):
        dwg = svgwrite.Drawing('badge.svg', profile='tiny')
        path = svgwrite.path.Path()
        path.push('M 0,45 C 0,47.5 2.5,50 5,50')
        path.push('L 5,50 150,50')
        path.push('L 150,50 150,0')
        path.push('L 150,0 5,0')
        path.push('C 2.5,0 0,2.5 0,5')
        path.push('Z')
        dwg.add(path)
        dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
        dwg.save()

    def __call__(self):
        pass

if __name__ == "__main__":
    badge_generator = BadgeGenerator()