import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle-Daryna-Kosyk",
    version="0.0.1",
    author="Daryna Kosyk",
    author_email="daryna.kosyk@ucu.edu.ua",
    description="A package to check if the board for the number game is valid.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
