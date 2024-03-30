from setuptools import setup, find_packages

setup(
    name='simulatedpeople',
    version='0.1.0',
    description='A Python class for creating simulated conversation partners powered by OpenAI',
    author='RejektsAI',
    author_email='santillansat@gmail.com',
    url='https://github.com/RejektsAI/simulatedpeople',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
)
