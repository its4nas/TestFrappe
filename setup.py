from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in programming_test/__init__.py
from programming_test import __version__ as version

setup(
	name="programming_test",
	version=version,
	description="Programming Company Test",
	author="My Team",
	author_email="team@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
