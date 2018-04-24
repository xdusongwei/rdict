from setuptools import setup

setup(
    name='rdict',
    version='0.1.0',
    author='songwei',
    author_email='songwei@songwei.io',
    description='A Pythonic tool is used for operating redis commands.',
    long_description='',
    url='https://github.com/xdusongwei/rdict',
    python_requires='>=3',
    packages=['rdict'],
    ext_modules=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    install_requires=["redis"],
)
