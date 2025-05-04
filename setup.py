'''
The setup.py file is an essential part of packageing and
distributing Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your projects, such as its metadata, dependencies, and more...
'''
from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read Lines from file
            lines = file.readlines()
            #Process Each line
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e .
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)
    except Exception as e:
        print("requirement.txt file not found")
        
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Abhineash Kishan",
    author_email="avikishan002@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()
)