#!/usr/bin/python

from distutils.core import setup
setup(
    name='telephus',
    version='1.0.0beta1',
    description='connection pooled, low-level client API for Cassandra in Twisted python',
    author='brandon@faltering.com',
    url='http://github.com/driftx/Telephus',
    packages=['telephus',
              'telephus.cassandra',
              'telephus.cassandra.c07',
              'telephus.cassandra.c08']
)
