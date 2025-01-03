from setuptools import setup, find_packages

setup(
    name='saidata',
    version='1.0.0',
    description='Mini-Dashboard Terminal pour la Surveillance du Système en Temps Réel',
    author='Said Laachir',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'rich',
        'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'saidata=saidata.mainCode:main',  # chemin vers votre fonction `main`
        ],
    },
)