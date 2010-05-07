from setuptools import setup, find_packages
 
setup(name='aupostcodes',
    version='0.1',
    description=open('README').read(),
    long_description=open('README').read(),
    author='Jeremy Epstein',
    author_email='jazepstein@gmail.com',
    url='http://github.com/Jaza/aupostcodes',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ]
)
