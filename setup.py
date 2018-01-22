from setuptools import setup, find_packages

setup(
	name='data-analysis',
	version='0.0.1',
	url='www.github.com',
	license='BSD',
	packages=find_packages(),
	install_requires=[
						'pyqt5',
						'pandas',
						'sqlalchemy',
						'nltk',
						'numpy',
						'jupyter',
						'python-twitter'],
	entry_points={},
	extras_require={'dev': ['flake8',]},
	)
