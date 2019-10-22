import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="persipy",
    version="0.0.1",
    author="Pavel V. Pristupa",
    author_email="pristupa@gmail.com",
    description="Persistence API for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pristupa/persipy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License version 3.0 (GPL-3.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)