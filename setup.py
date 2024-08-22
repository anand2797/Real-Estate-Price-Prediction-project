from setuptools import setup, find_packages
from typing import List

hiphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]: # here return list having string
    '''
    This fuction returns the libraries and packages which are present in 
    requirements.txt '''
    requirements = []

    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [i.strip() for i in requirements]
        
        if hiphen_e_dot in requirements:
            requirements.remove(hiphen_e_dot)
    return requirements


setup(
    name = 'Real-Estate-Price-Prediction',
    version= '0.0.1',
    author= 'Talware Anand',
    author_email='anandtalware27@gmail.com',
    packages= find_packages(),
    install_requires  = get_requirements('requirements.txt')

    )