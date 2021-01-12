import argparse
import svgwrite
from svgwrite.shapes import Line

class BadgeGenerator:
    def __init__(self):
        dwg = svgwrite.Drawing('badge.svg', profile='tiny')
        path = svgwrite.path.Path()
        #path.push(Line(start=(0,0), end=(0, 2.5)))
        #path.push_arc(target=(0.5, 3.0), rotation=0.0, r=0.5, absolute=True, large_arc=False)
        path.push('M 0,2.5 c 0,2.75 0.25,3.0 0.5,3.0')
        dwg.add(path)
        dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
        dwg.save()

    def __call__(self):
        pass

if __name__ == "__main__":
    badge_generator = BadgeGenerator()