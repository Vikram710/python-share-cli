from setuptools import setup

setup(
    name="mycli",
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'sqlalchemy'
    ],
    entry_points='''
        [console_scripts]
        mycli=cli:cli
    ''',
)
