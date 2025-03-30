from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='g2o',
    version='0.0.9',
    package_dir={'g2o': 'g2o'},  # Maps the 'g2o' package to the 'g2o' directory
    packages=['g2o'],  # Explicitly specify the package instead of relying on find_packages()
    include_package_data=True,  # Ensures non-Python files (e.g., .so, .a) are included
    package_data={
        'g2o': ['*.so', '*.a', '*.pyi'],  # Include .so, .a, and .pyi files in the g2o package
    },
    description='g2o for Python',
    author='ubicoders',
    author_email='info@ubicoders.com',
    url='https://github.com/ubicoders/g2opy',
    keywords='g2o, SLAM, BA, ICP, optimization, python, binding',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['numpy'],  # Add dependencies like numpy if needed
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust license as needed
        'Operating System :: POSIX :: Linux',
    ],
)