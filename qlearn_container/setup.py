from setuptools import setup
from setuptools import find_packages

install_requires = [
    'Keras'
]

setup(
      name='qlearncatchd3',
      version='0.0.1',
      description='Q-learning for Keras with D3 view',
      author='Fariz Rahman',
      author_email='farizrahman4u@gmail.com',
      url='https://github.com/farizrahman4u/qlearning4k',
      license='GNU GPL v2',
      install_requires=install_requires,
      packages=find_packages()
)
