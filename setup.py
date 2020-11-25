from setuptools import setup

setup(name='py_server',
      version='1.0',
      description='Expose your filesystem to local-network',
      url='https://github.com/priyansh-anand/',
      author='Priyansh Anand',
      author_email='pr1y4nsh@protonmail.com',
      license='MIT',
      packages=['py_server'],
      install_requires=[
          'flask',
          'gunicorn'
      ],
      zip_safe=False)
