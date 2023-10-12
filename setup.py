from setuptools import find_packages, setup

setup(
    name="scenicNL",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "scenic==3.0.0b2",
    ],
    entry_points={
        "console_scripts": [
            "gen_scenes=main.__main__:_launch",
        ],
    },
    extras_require={
        "dev": [
            "black",
            "pytest",
            "isort",
            "mock",
            "pytest-mock",
            "beautifulsoup4",
        ],
    },
    python_requires=">=3.11",
    author="Karim Elmaaroufi",
    author_email="k.e@berkeley.edu",
    description="Generate simulator scenes using Scenic from natural language descriptions.",
    long_description=open("README.md").read(),
    url="https://github.com/ke7/scenicNL",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.11",
    ],
)