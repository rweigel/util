from setuptools import setup, find_packages

# Need requests_cache 1.2 because of
# https://github.com/requests-cache/requests-cache/issues/927
# and fact that hpde.io returns json with
# "Content-Type": "application/json; charset=utf-8"
# (charset=utf-8 is redundant and causes requests_cache not not cache
# _decoded_content)
# See also utilrsw/get_json.py/_requests_cache_bug()
install_requires = [
    "requests_cache==1.2",
    "deepdiff"
]

setup(
    name='utilrsw',
    version='0.0.1',
    author='Bob Weigel',
    author_email='rweigel@gmu.edu',
    packages=find_packages(),
    license='LICENSE.txt',
    description='Misc utility functions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=install_requires
)
