from setuptools import setup

setup(
	name='flaskapp',
	packages=['flaskapp'],
	include_package_data=True,
	install_requires=[
	'flask==0.12.2',
	'flask-login==0.2.7',
	'sqlalchemy==0.8.2',
	'flask-sqlalchemy==1.0'
	],

)
