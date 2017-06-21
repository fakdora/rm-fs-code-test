from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
]

setup(name='sampleapp_be',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = sampleapp_be:main
      """,
)
