from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='cli-weather',
    version='0.1.2',    
    description='Lightweight command line app to get fast weather data right on the command line',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vatsa287/cli-weather',
    author='Shree Vatsa N',
    author_email='i.mnshreevatsa@gmail.com',
    license='GPL 3.0',
    packages=['cli_weather'],
    install_requires=['requests'],
    entry_points = {
        'console_scripts': [
            'cli-weather=cli_weather.main:main'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.3",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Natural Language :: English"
    ],
)
