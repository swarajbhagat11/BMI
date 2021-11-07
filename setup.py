from setuptools import setup, find_packages

with open('README') as f:
    readme = f.read()

setup(
    name='bmi_calculator',
    version='0.1.0',
    description='This package is to calculate BMI based on height and weight.',
    long_description=readme,
    author='Swaraj Bhagat',
    author_email='swarajbhagat11@gmail.com',
    url='https://github.com/swarajbhagat/bmi_calculator',
    packages=find_packages(exclude=('tests'))
)