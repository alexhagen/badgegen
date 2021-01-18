"""BadgeGeneration Module."""
import argparse
import svgwrite
from svgwrite.shapes import Line

class BadgeGenerator:
    """Badge Generator."""
    def __init__(self):
        """Initialize the badge generator and write out the outline."""
        self.dwg = svgwrite.Drawing('badge.svg', profile='tiny')
        self.left_rectangle()
        self.right_rectangle()
        self.dwg.add(self.dwg.text('Test', insert=(75.0/2.0, 25.0/2.0), fill='red'))
        self.dwg.save()

    def __call__(self):
        pass

    def left_rectangle(self, width=75.0, height=25.0, radius=5.0):
        path = svgwrite.path.Path()
        path.push(f'M 0.0,{height - radius} C 0.0,{height - radius/2} {radius/2.0},{height} {radius},{height}')
        path.push(f'L {radius},{height} {width},{height}')
        path.push(f'L {width},{height} {width},0.0')
        path.push(f'L {width},0 {radius},0')
        path.push(f'C {radius/2.0},0 0,{radius/2.0} 0,{radius}')
        path.push('Z')
        self.dwg.add(path)

    def right_rectangle(self, width=150.0, height=25.0, radius=5.0, corner=75.0):
        path = svgwrite.path.Path(fill='red')
        path.push(f'M {corner + width - radius},{height} C {corner + width - radius/2.0},{height} ' +
                  f'{corner + width},{height - radius/2.0} {corner + width},{height - radius}')
        path.push(f'L {corner + width},{height - radius} {corner + width},{radius}')
        path.push(f'C {corner + width},{radius/2.0} {corner + width - radius/2.0},0 {corner + width - radius},0')
        path.push(f'L {corner + width - radius},0 {corner},0')
        path.push(f'L {corner},0 {corner},{height}')
        path.push('Z')
        self.dwg.add(path)

if __name__ == "__main__":
    badge_generator = BadgeGenerator()