#!/usr/bin/env python
"""
Colab Edemocracia Colab plugin
===================================
"""
from setuptools import setup, find_packages

install_requires = [
    'colab',
    'django-bower',
    'django-compressor==1.6',
    'django-libsass'
]

tests_require = ['mock']


setup(
    name="colab_edemocracia",
    version='0.1.0',
    author='labhackercd',
    author_email='labhackercd@gmail.com',
    url='https://github.com/labhackercd/colab-edemocracia-plugin',
    description='Colab Edemocracia Colab plugin',
    long_description=__doc__,
    license='gpl3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    test_suite="tests.runtests.run",
    tests_require=tests_require,
    extras_require={'test': tests_require},
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)