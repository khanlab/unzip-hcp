import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unzip-hcp", # Replace with your own username
    version="0.0.1",
    author="Ali Khan",
    author_email="alik@robarts.ca",
    description="Simple tool for unzipping hcp packages, using a config file to select files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khanlab/unzip-hcp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'pandas>=1.0.0',
        'PyYAML>=5.3'],
    scripts=['unzip-hcp.py'],
)
