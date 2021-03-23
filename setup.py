import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="usim800_hamilkar",
    version="0.0.2.1",
    author="hamilkar247",
    author_email="adonnibal96@gmail.com",
    description="usim800_hamilkar is a Python driver module for SIM800 GSM/GPRS .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hamilkar247/usim800_hamilkar",
    packages=setuptools.find_packages(include=['usim800_hamilkar',],exclude=("tests",)),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    license = "MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires = ['pyserial']
)
