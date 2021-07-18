import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CocuniRandom",
    version="0.1",
    author="Jorge Riveros",
    author_email="christian.riveros@outlook.com",
    description='A Python package for cocuni random numbers generation',
    url="https://github.com/pypa/amira-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
