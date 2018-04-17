# Library dependencies for the python code.  You need to install these with
# `pip install -r requirements.txt` before you can run this.

#### ESSENTIAL LIBRARIES FOR MAIN FUNCTIONALITY ####
from setuptools import setup
from setuptools import find_packages


setup(name='dltext',
      version='1.0',
      description='preprocessing text for deep learning',
      author='',
      author_email='',
      url='https://github.com/YasserMustafa/DL-text',
      #download_url='',
      license='MIT',
      #install_requires=['numpy>=1.9.1',
                        'scipy>=0.14',
                        'six>=1.9.0',
                        'pyyaml',
                        'h5py'],
                        
      #extras_require={
          'visualize': ['pydot>=1.2.4'],
          'tests': ['pytest',
                    'pytest-pep8',
                    'pytest-xdist',
                    'pytest-cov',
                    'pandas',
                    'requests'],
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      packages=find_packages())
