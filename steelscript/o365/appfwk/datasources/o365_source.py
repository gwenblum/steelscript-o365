# steelscript/o365/appfwk/datasources/o365_source.py
# Version: 20160514 V03
# Gwen Blum; gwen.blum@gmail.com
# Description: Office365 Reports source
# Changelog:
# 20160514 Gwen : add MailboxUsageTable - office365 mailbox usage report
#

# Copyright (c) 2015 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the MIT License
# accompanying the software ("License").  This software is distributed "AS IS"
# as set forth in the License.

"""
This file defines a data source for querying data.

There are three parts to defining a data source:

* Defining column options via a Column class
* Defining table options via a DatasourceTable
* Defining the query mechanism via a Query class

Note that you can define multiple Column and Table classes
in the same file. Each Table class needs to associate with a
Query class by specifying the _query_class attribute.

"""

import logging
import pandas

from steelscript.common.timeutils import \
    datetime_to_seconds, timedelta_total_seconds, parse_timedelta

from steelscript.appfwk.apps.datasource.models import \
    DatasourceTable, Column

from steelscript.appfwk.apps.datasource.modules.analysis import \
    AnalysisTable, AnalysisQuery

from steelscript.appfwk.apps.devices.forms import fields_add_device_selection
from steelscript.appfwk.apps.devices.devicemanager import DeviceManager
from steelscript.appfwk.apps.datasource.forms import (fields_add_time_selection,
                                                      fields_add_resolution)
from steelscript.appfwk.apps.datasource.models import TableQueryBase

from steelscript.o365.core.app import get_MailBoxUsage
from steelscript.o365.core.app import get_MailBoxUsage_TEST

logger = logging.getLogger(__name__)

###############################
#### Mailbox Usage
###############################

class O365MailboxUsageColumn(Column):
    class Meta:
        proxy = True
    COLUMN_OPTIONS = { }

class O365MailboxUsageTable(DatasourceTable):

    class Meta:
        proxy = True
    _column_class = 'O365MailboxUsageColumn'
    _query_class = 'O365MailboxUsageQuery'
    TABLE_OPTIONS = { }
    FIELD_OPTIONS = { }

    def post_process_table(self, field_options):
        pass

class O365MailboxUsageQuery(TableQueryBase):

    def run(self):
        criteria = self.job.criteria
	self.data = pandas.DataFrame( get_MailBoxUsage('','','','') )
	return True

