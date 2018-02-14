try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Find Phone Number in a Passed String',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/isPhoneNumber',
	'download_url': 'https://github.com/sunnylam13/isPhoneNumber',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'isPhoneNumber'
}

setup(**config)