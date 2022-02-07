from setuptools import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='ipyturtle3',
    version='0.1.1',    
    description='Turtle graphics based on ipycanvas which can run on jupyter lab/vscode. ',
    url='https://github.com/williamnavaraj/ipyturtle3.git',
    author='William Navaraj',
    author_email='williamnavaraj@gmail.com',
    license='Apache 2.0',
    packages=['ipyturtle3'],
    install_requires=['ipycanvas',
                      'webcolors'
                      ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: Apache Software License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)