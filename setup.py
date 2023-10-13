# setup.py
from setuptools import setup, find_packages

setup(
    name="albert",
    version="0.1e",
    packages=find_packages(),
    install_requires=[
        # Liste suas dependências aqui, por exemplo:
        # "numpy>=1.18",
        # "matplotlib>=3.2"
    ],
    entry_points={
        "console_scripts": [
            "albert = albert.albert:main"
        ]
    },
    author="Heber A. Scachetti",
    author_email="heber.augusto@gmail.com",
    description="Uma biblioteca Python para facilitar a criação de pipelines de modelos de Generative AI",
    license="MIT",
    keywords="biblioteca python comando",
    url="https://github.com/heber-augusto/albert",
)
