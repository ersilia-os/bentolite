import setuptools

install_requires = ["werkzeug", "click", "requests", "multidict", "aiohttp"]

setuptools.setup(
    name="bentolite",
    version="0.0.0",
    author="Ersilia Open Source Initiative",
    author_email="miquel@ersilia.io",
    description="A lite version of early BentoML to be used by Ersilia",
    long_description="A lite version of early BentoML to be used by Ersilia",
    license="Apache License 2.0",
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    url="https://github.com/ersilia-os/bentolite",
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.6.1",
    entry_points={"console_scripts": ["bentolite=bentolite.cli:cli"]},
    project_urls={
        "Bug Reports": "https://github.com/ersilia-os/ersilia/issues",
        "Source Code": "https://github.com/ersilia/bentolite",
    },
    include_package_data=False,
)
