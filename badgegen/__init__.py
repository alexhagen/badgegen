import argparse
import svgwrite

class BadgeGenerator:
    def __init__(self):
        dwg = svgwrite.Drawing('badge.svg', profile='tiny')
        dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
        dwg.save()

    def __call__(self):
        pass

if __name__ == "__main__":
    pass