from setuptools import setup

setup(name='mailtmapi',
      version='1.1',
      description='Python API wrapper for mail.tm',
      packages=['mailtm'],
      author_email='coder@derkown.ru',
      zip_safe=False,
      url='https://github.com/prtolem/MailTM',
      install_requires=[
            'aiohttp==3.8.1'
            'pydantic==1.10.2',
      ])
