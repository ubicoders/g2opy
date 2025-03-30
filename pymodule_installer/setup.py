from setuptools import setup

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='g2o',
    version='0.0.9',
    packages=[''],  # Empty string means the root directory is the module
    package_dir={'': 'g2o'},  # Map the root package to the 'g2o' directory
    include_package_data=True,
    package_data={
        '': ['*.so', '*.a', '*.pyi'],  # Include .so, .a, and .pyi files at the root
    },
    description='g2o for Python',
    author='ubicoders',
    author_email='info@ubicoders.com',
    url='https://github.com/ubicoders/g2opy',
    keywords='g2o, SLAM, BA, ICP, optimization, python, binding',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust license as needed
        'Operating System :: POSIX :: Linux',
    ],
)