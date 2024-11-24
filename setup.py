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
        'setuputils'
    ],
    entry_points={
        'console_scripts': [
            'saidata=saidata.saidata:main',  # chemin vers votre fonction `main`
        ],
    },
)