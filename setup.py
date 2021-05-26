import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MHDpy",
    version="0.0.1",
    author="Wenyin Wei",
    author_email="wenyin.wei@ipp.ac.cn",
    description="MHDpy handles the geometry and fields of physical quantities in magnetically confined fusion.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WenyinWei/MHDpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)