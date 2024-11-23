from setuptools import setup, find_packages

setup(
    name='saidata',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'psutil','rich', 'pynput','keyboard'  # Example dependency
    ],
    entry_points={
        'console_scripts': [
            'saidata = saidata.saidata:main',  # The command `saidata` will run the `main` function in `saidata.py`
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
