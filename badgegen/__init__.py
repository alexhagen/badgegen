"""BadgeGeneration Module."""
import argparse
import svgwrite
from svgwrite.shapes import Line

class BadgeGenerator:
    """Badge Generator."""
    def __init__(self, left_width=150, right_width=150, left_text='test',
                 right_text='100%', height=50, radius=5):
        """Initialize the badge generator and write out the outline."""
        self.dwg = svgwrite.Drawing('badge.svg', profile='tiny')
        self.left_rectangle(left_width, height, radius)
        self.right_rectangle(right_width, height, radius, left_width)
        self.dwg.add(self.dwg.text(left_text, insert=(left_width/2.0, height/2.0), fill='red'))
        self.dwg.add(self.dwg.text(right_text, insert=(left_width + right_width/2.0, height/2.0), fill='red'))
        
    def __call__(self):
        self.dwg.save()

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

def _get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--left-width', default=150, nargs='?',
                        help='Width of the left cell, ``None`` if fit to text')
    parser.add_argument('--right-width', default=150, nargs='?',
                        help='Width of the left cell, ``None`` if fit to text')
    parser.add_argument('--left-text', default='test', nargs='?',
                        help='Text for the left cell. Can be python format string')
    parser.add_argument('--right-text', default='100%', nargs='?',
                        help='Text for the right cell.  Can be python format string')
    return parser

def _run_cli():
    args = _get_argparser().parse_args()
    badge_generator = BadgeGenerator(**vars(args))
    badge_generator()

if __name__ == "__main__":
    _run_cli()