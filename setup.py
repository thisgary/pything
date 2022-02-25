import setuptools

#readme = open('README.md').read() 
#requirements = open('requirements.txt').read().splitlines()

setuptools.setup(
        name='pything',
        version='0.0.7',
        author='thisgary',
        author_email='gary.github@gmail.com',
        description='Something Python.',
#        long_description=readme,
        long_description_content_type='text/markdown',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT Lisence',
            'Operating System :: OS Independent',
        ],
        license='MIT',
        python_requires='>=3.8',
#        install_requires=requirements,
        setup_requires=['pytest_runner'],
        tests_require=['pytest'],
        test_suite='tests',
)
