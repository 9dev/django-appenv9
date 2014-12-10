import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-{{ NAME }}',
    version='0.1',
    packages=['{{ SAFE_NAME }}'],
    include_package_data=True,
    license='MIT License',
    description='Another Django app', # @todo app description
    long_description=README,
    url='{{ URL }}',
    author='{{ AUTHOR_NAME }}',
    author_email='{{ AUTHOR_EMAIL }}',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
	install_requires = [
		'django >= {{ DJANGO_VERSION }}',
    ],
)
