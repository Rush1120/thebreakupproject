from setuptools import setup, find_packages

setup(
    name='thebreakupproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'textblob',
        'matplotlib',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'breakup-journal=breakup_journal.main:main'
        ]
    },
    author='Rushikalia',
    description='A terminal-based breakup journal with emotion tracking.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rush1120/thebreakupproject',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
