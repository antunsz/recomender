from setuptools import setup, find_packages

setup(
    name='recomender',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'pandas',
        'numpy',
    ]
)
