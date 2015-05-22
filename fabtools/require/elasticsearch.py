"""
Elasticsearch
=============

This module provides high-level tools for installing an elasticsearch
server.

"""
import fabtools

def server(version=None):
    """
    Require a elasticsearch server to be installed and running.

    Example::

        from fabtools import require

        require.elasticsearch.server()

    """
    fabtools.elasticsearch.install(version)
    fabtools.require.service.started('elasticsearch')
