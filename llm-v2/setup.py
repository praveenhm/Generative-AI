import os
from setuptools import setup, find_packages
from typing import AnyStr


def read(fname: str) -> AnyStr:
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="llm",
    version="1.0.0",
    author="Asif Qamar",
    author_email="asif@supportvectors.com",
    description="Text-extraction from given file.",
    url="https://packages.python.org/svlearn-bootcamp",
    packages=find_packages(),
    # packages=find_packages(where='.', include=['llm-v2.svlearn*', 'ImageBind.imagebind*']),
    long_description=read('README.md'),
    classifiers=["Operating System::OS Independent"],
)
"""
# Capture the packages
discovered_packages = find_packages(where='.')

# Print the discovered packages
print("Discovered packages:--------------------", discovered_packages)

setup(
    packages=discovered_packages,
    package_dir={
        'svlearn': 'llm-v2/svlearn',
        'imagebind': 'ImageBind/imagebind'
    },  
)
print("---------------packages---------------")

"""
 