from setuptools import find_packages, setup
from typing import List
# This file is resposible for defining the configuration of the package
# as well as the dependencies that are required for the package to run. 
def get_requirements()->List[str]:
    requirement_list: List[str] = []
    try:
        with open("requirements.txt") as file:
            lines=file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore the empty lines and -e .
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_list
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Shubham Mishra",
    author_email="mshubham.mishra18@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)