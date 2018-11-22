from setuptools import setup, find_packages

setup(name='donkeypart_differential_drive',
      version='0.1',
      description='Motor controls for creating a differential drive robot.',
      long_description="no long description given",
      url='https://github.com/autorope/donkeypart_differential_drive',
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',
      install_requires=[
          'Adafruit_MotorHAT@ https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library/archive/master.zip'
          ],
      extras_require={'dev': ['pytest-cov']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars motors',
      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
