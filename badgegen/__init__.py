"""BadgeGeneration Module."""
import argparse
import svgwrite
from svgwrite.shapes import Line

class BadgeGenerator:
    """Badge Generator."""
    def __init__(self):
        """Initialize the badge generator and write out the outline."""
        dwg = svgwrite.Drawing('badge.svg', profile='tiny')
        path = svgwrite.path.Path()
        w = 75.0
        r = 5.0
        h = 25.0
        path.push(f'M 0.0,{h - r} C 0.0,{h - r/2} {r/2.0},{h} {r},{h}')
        path.push(f'L {r},{h} {w},{h}')
        path.push(f'L {w},{h} {w},0.0')
        path.push(f'L {w},0 {r},0')
        path.push(f'C {r/2.0},0 0,{r/2.0} 0,{r}')
        path.push('Z')
        dwg.add(path)
        path = svgwrite.path.Path(fill='red')
        lw = w
        rw = 150.0
        path.push(f'M {lw + rw - r},{h} C {lw + rw - r/2.0},{h} ' +
                  f'{lw + rw},{h - r/2.0} {lw + rw},{h - r}')
        path.push(f'L {lw + rw},{h - r} {lw + rw},{r}')
        path.push(f'C {lw + rw},{r/2.0} {lw + rw - r/2.0},0 {lw + rw - r},0')
        path.push(f'L {lw + rw - r},0 {lw},0')
        path.push(f'L {lw},0 {lw},{h}')
        path.push('Z')
        dwg.add(path)
        dwg.add(dwg.text('Test', insert=(lw/2.0, hw/2.0), fill='red'))
        dwg.save()

    def __call__(self):
        pass

if __name__ == "__main__":
    badge_generator = BadgeGenerator()