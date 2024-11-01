from setuptools import find_packages,setup

setup(
    name = "mcq_generator",
    version='0.0.1',
    author='Dareeul',
    author_email='dulyarit.lua@gmail.com',
    install_requires = ["langchain","transformers","streamlit","PyPDF2"],
    packages=find_packages()

)