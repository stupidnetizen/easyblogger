import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name="EasyBlogger",
      version="0.9.4",
      author="Raghu Rajagopalan",
      author_email="raghu.nospam@gmail.com",
      description=("A (very) easy CLI interface to Blogger blogs"),
      license="BSD",
      keywords="blogger, cli",
      url="https://github.com/raghur/easyblogger",
      packages=['blogger'],
      install_requires=[
          'pypandoc',
          'google-api-python-client',
          'python-gflags',
          'httplib2'
      ],
      entry_points={
          'console_scripts': [
              'easyblogger = blogger.blogger:main'
          ]
      },
      long_description=readme(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: BSD License",
      ],
      )
