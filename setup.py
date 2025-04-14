from setuptools import setup, find_packages

setup(
    name="image-captioning",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-multipart",
        "Pillow",
        "torch",
        "transformers",
        "nltk",
        "keybert"
    ],
) 