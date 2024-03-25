from setuptools import setup,find_packages
from typing import List

HYP="-e ."
def get_dependencies(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req  in requirements]
        if HYP in requirements:
            requirements.remove(HYP)
    return requirements
    


setup(
    name='mlproject',
    version='0.0.1',
    author='ashik',
    author_email='datas293@gmail.com',
    packages=find_packages(),
    install_requires=get_dependencies('requirements.txt'),
)