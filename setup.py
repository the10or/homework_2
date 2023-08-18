from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',
    version='1.0.0',
    description='folder cleaning utility',
    url='https://github.com/the10or/homework_2',
    author='the10or',
    author_email='the10or@gmail.com',
    packages=find_namespace_packages(),
    package_dir={"": "."},
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']}

)
