from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='g2o',
    version='0.0.1',
    # Remove package_dir to avoid remapping; let find_packages handle it
    packages=['g2o'],  # Explicitly specify the 'g2o' package
    # Include all relevant files in the g2o package
    package_data={
        'g2o': [
            'g2o/*.pyi'  # Files in the nested g2o/g2o directory
        ],
    },
    include_package_data=True,  # Ensures package_data is respected
    description='g2o for python',
    author='ubicoders',
    keywords='g2o, SLAM, BA, ICP, optimization, python, binding',
    author_email='info@ubicoders.com',
    url='https://github.com/ubicoders/g2opy',
    long_description=long_description,
    long_description_content_type='text/markdown',
)