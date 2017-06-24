from setuptools import setup, find_packages

description = "This is a set of packages and scripts that provide a simple way for interfacing with the Tanium SOAP API using python or the command line."
setup(
    name='pytan',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    url='http://tanium.github.io/pytan',
    license='MIT',
    author='Jim Olsen',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: Implementation :: CPython",
        "Natural Language :: English"
    ],
    author_email='jim.olsen@tanium.com',
    description=description,
    long_description=description,
    packages=find_packages("."),
    platforms='any'
)
