from setuptools import setup, find_packages

setup(
    name="textflip",
    version="0.3.0",
    install_requires=[
        "regex",
    ],
    author="L3viathan",
    author_email="git@l3vi.de",
    description="Flip text by 180°",
    url="https://github.com/L3viathan/textflip",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
