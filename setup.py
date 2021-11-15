from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ub/__init__.py
from ub import __version__ as version

setup(
	name="ub",
	version=version,
	description="Custom App For UB",
	author="ERP Cloud Systems",
	author_email="info@erpcloud.systems",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
