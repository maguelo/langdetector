from setuptools import setup, find_packages

setup(
    name="langtoolkit",  # Nombre del paquete/distribución
    version="0.1",  # Versión del paquete
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=[
        "unidecode",
        "spacy==3.6",
        'tqdm',
        'nltk'
    ],
    include_package_data=True,
    author="Miguel Maldonado",
    description="Tools for working with natural language",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maguelo/langtoolkit",  # URL del repositorio o página del proyecto
    python_requires=">=3.9",  # Requerimiento de versión de Python
)
