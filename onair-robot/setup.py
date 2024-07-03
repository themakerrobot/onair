from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
]

test_requirements = [
]

setup(
    name='onair-robot',
    version='0.0.0',
    description="onair",
    long_description=readme,
    author="circulus",
    author_email='leeyunjai@circul.us',
    url='https://github.com/themakerrobot/onair-project',
    packages=[],
    package_dir={},
    package_data={},
    install_requires=requirements,
    zip_safe=False,
    keywords='onair',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
