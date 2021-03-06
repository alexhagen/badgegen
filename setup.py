from setuptools import setup
from setuptools import find_packages


setup(name='badgegen',
      version=0.2,
      description='CI/CD Badge Generator',
      author='Alex Hagen',
      author_email='alexhagen6@gmail.com',
      url='https://github.com/alexhagen/badgegen',
      long_description=open('README.md').read(),
      packages=['badgegen'],
      scripts=['bin/badgegen'],
      install_requires=['svgwrite']
     )
