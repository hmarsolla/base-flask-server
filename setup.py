try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'my_api',
    'author': 'Heitor Marsolla',
    'url': '',
    'download_url': '',
    'author_email': 'hmarsolla@hotmail.com',
    'version': '1.0',
    'install_requires': [
        'requests==2.21.0',
        'schedule==0.5.0',
        'flask==1.0.2',
        'flask-cors==3.0.7',
        'waitress==1.1.0',
        'cryptography==2.4.2',
        'pyjwt==1.7.1',
    ],
    'packages': ['my_api'],
    'scripts': [],
    'name': 'my_api'
}

setup(**config, include_package_data=True)