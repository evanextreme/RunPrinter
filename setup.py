"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='runprinter',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    python_requires='>=3.5',
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
