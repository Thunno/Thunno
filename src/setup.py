from setuptools import setup, find_packages

long_description = 'Thunno is an ASCII-based golfing language written in Python. It has over 400 commands. Learn more at https://github.com/Thunno/Thunno'

setup(
  name = 'thunno',
  version = '1.2.0',
  license='MIT',
  description = 'An ASCII-based golfing language',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/Thunno/Thunno',
  download_url = 'https://github.com/Thunno/Thunno/archive/refs/tags/v1.2.0.tar.gz',
  keywords = ['golfing', 'code-golf', 'language'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
        'thunno = thunno.main:cmdline'
    ]
  }
)
