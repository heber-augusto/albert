# setup.py
from setuptools import setup, find_packages

setup(
    name="albert",
    version="0.1rc3",
    packages=find_packages(),
    install_requires=[
        "setuptools-git",
    ],
    entry_points={
        "console_scripts": [
            "albert = albert.albert:main"
        ]
    },
    include_package_data=True,
    author="Heber A. Scachetti",
    author_email="heber.augusto@gmail.com",
    description="Uma biblioteca Python para facilitar a criação de pipelines de modelos de Generative AI",
    license="MIT",
    keywords="biblioteca python comando",
    url="https://github.com/heber-augusto/albert",
)
