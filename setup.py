from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='oscer',
      version='0.1',
      author='Bruno Gola',
      author_email='me@bgo.la',
      description='A very simple command line OpenSoundControl sender',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/bgola/oscer",
      packages=find_namespace_packages(include=['oscer']),
	  classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Operating System :: OS Independent",
      ],
	  install_requires=['python-osc==1.7.4'],
      keywords='udp osc opensoundcontrol',
      python_requires='>=3.7',
      scripts=[
              'scripts/oscer',
          ],
      )
