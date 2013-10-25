from distutils.core import setup

setup(
    name='ccm',
    version='1.0.0',
    author='tcstewar',
    author_email='tcstewar@github.com',
    packages=['ccm', 'ccm.display', 'ccm.display.cairo', 'ccm.display.pygame', 'ccm.display.tk', 'ccm.legacy', 'ccm.lib', 'ccm.lib.actr', 'ccm.lib.nef', 'ccm.ui', 'ccm.tests'],
    url='https://github.com/tcstewar',
    license='LICENSE.txt',
    description='Python cognitive modeling suite',
    long_description=open('README.txt').read(),
    install_requires=[],
)
