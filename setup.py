from setuptools import setup, find_packages

version = '1.9'

setup(
    name='cmsplugin-fbalbumlight',
    version=version,
    description='facebook album plugin for django-cms with lightbox',
    author='Vinit Kumar',
    author_email='vinit.kumar@changer.nl',
    url='http://github.com/vinitcool76/cmsplugin-fbalbum.git',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
