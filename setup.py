from setuptools import setup, find_packages     #find all packages which are available in the entire ML application / directory which we have created 
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' 
    this function will retun the list of requirements  
    '''
    requirements=[]
    with open(file_path) as file_obj: 
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if  HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
name='MLOPS', 
version='1.0',
author='Johnas',
author_email='johnas1433@yahoo.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)