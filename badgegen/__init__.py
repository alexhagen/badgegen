import argparse
import svgwrite

class BadgeGenerator:
    def __init__(self):
        dwg = svgwrite.Drawing('badge.svg', profile='tiny')
        path = svgwrite.path.Path()
        path.push(*elements)
        path.push_arc(t)
        dwg.add(path)
        dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
        dwg.save()

    def __call__(self):
        pass

if __name__ == "__main__":
    pass