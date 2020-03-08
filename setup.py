from setuptools import setup, find_packages

setup(
   name='PyChummer',
   version='1.0',
   description='A PyQt5 based characer management tool for Shadowrun',
   author='Adam Ness',
   author_email='adam.ness@gmail.com',
   packages=find_packages(),
   install_requires=['PyQt5==5.14.1'], #external packages as dependencies
   scripts=['scripts/pychummer'],
   package_data={
       "": ["README.md", "LICENSE"]
   }
)