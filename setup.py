from setuptools import setup

setup(
    name='ipyturtle3',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/williamnavaraj/ipyturtle3.git',
    author='William Navaraj',
    author_email='williamnavaraj at gmail dot com',
    license='Apache 2.0',
    packages=['ipyturtle3'],
    install_requires=['ipycanvas',
                      'webcolors'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        'License :: Apache 2.0',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)