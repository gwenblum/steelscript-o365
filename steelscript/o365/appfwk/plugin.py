# Copyright (c) 2015 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the MIT License
# accompanying the software ("License").  This software is distributed "AS IS"
# as set forth in the License.

import pkg_resources

from django.apps import AppConfig

from steelscript.appfwk.apps.plugins import Plugin as AppsPlugin


class Plugin(AppsPlugin):
    title = 'Office365 Usage'
    description = 'Office 365 Usage App Framework Plugin'
    version = pkg_resources.get_distribution('steelscript.o365').version
    author = 'Gwen Blum'

    enabled = True
    can_disable = True

    devices = ['devices']
    datasources = ['datasources']
    reports = ['reports']

    # List javascript/css files required by this plugin to work.
    # If a file is local to this plugin, it should be in /static/<path>.
    # Remote content can also be listed by fully qualified URL
    #
    # Example:
    #    js = ['/static/js/__plugin__.js',
    #          'http://some.website.com/cool.js']
    #    css = ['/static/css/__plugin__.css',
    #          'http://some.website.com/cool.css']
    #
    js = []
    cs = []


class SteelScriptAppConfig(AppConfig):
    name = 'steelscript.o365.appfwk'
    # label cannot have '.' in it
    label = 'steelscript_o365'
    verbose_name = 'Office365 Usage'
