from setuptools import find_packages, setup
from typing import List
HYPEN_e_DOT='e.'
def get_requirements(file_path:str)->List[str]:
    '''
    function return the list of requirments
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements ]
        if HYPEN_e_DOT in requirements:
            requirements.remove(HYPEN_e_DOT)
            return requirements
setup(
name='mlproject',
version='0.0.1',
author='Mohsin',
author_email='mohsin.raza.ali@outlook.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')





)