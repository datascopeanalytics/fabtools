"""
Elasticsearch
=============

This module provides tools for installing `elasticsearch`_.

.. _elasticsearch: http://www.elasticsearch.org/

"""
from fabric.api import sudo
import fabtools

DEFAULT_VERSION = '1.3'


def install(version=None, start_on_boot=True, start=True):
    """
    Install elasticsearch.

    ::

        import fabtools

        # Install elasticsearch
        fabtools.elasticsearch.install()


    """
    # use default version if None given
    if version is None:
        version = DEFAULT_VERSION

    family = fabtools.system.distrib_family()

    if family == 'debian':

        # we need Java. fuck.
        fabtools.require.oracle_jdk.installed()

        # download and install public signing key
        fabtools.require.deb.key(
            'D88E42B4',
            url='http://packages.elasticsearch.org/GPG-KEY-elasticsearch',
        )

        # add the source to enable the repository (this updates index)
        fabtools.require.deb.source(
            'elasticsearch',
            'http://packages.elasticsearch.org/elasticsearch/%s/debian' % version,
            'stable',
            'main',
        )

        # actually install repository
        fabtools.require.deb.package('elasticsearch')

        # optionally configure to start on boot
        if start_on_boot:
            start_server_on_boot()
        
        # start elasticsearch server
        if start:
            start_server()

    # nothing other than debian yet
    else:
        raise NotImplementedError(
            'This would be nice. See '
            'http://www.elasticsearch.org'
            '/guide/en/elasticsearch/reference/current/setup-repositories.html'
        )


def start_server_on_boot():
    """Configure to start elasticsearch server on boot.

    """
    sudo('update-rc.d elasticsearch defaults 95 10')


def start_server():
    """Start elasticsearch server.
    """
    sudo('/etc/init.d/elasticsearch start')

