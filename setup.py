from setuptools import setup, find_packages

setup(
    name='kryptos',
    version='0.1.0',
    description='Complete cryptographic library for all needs',
    author='iluzioDev',
    author_email='luischinearangel@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'coverage==5.5',
        'coveralls==3.3.1',
      ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
