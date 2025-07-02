import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fluent-appium",
    version="0.1.0",
    author="Geonwoo Lee",
    author_email="gwgwl1017@gmail.com",
    description="A fluent interface for Appium automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woori07/fluent-appium-python",
    project_urls={
        "Bug Reports": "https://github.com/woori07/fluent-appium-python/issues",
        "Source": "https://github.com/woori07/fluent-appium-python",
        "Documentation": "https://github.com/woori07/fluent-appium-python#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    keywords="For Appium automation testing fluent interface",
    zip_safe=False,
)