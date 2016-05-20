# steelscript/o365/appfwk/reports/o365_mbusage_report.py
# Version: 20160514 V05
# Author: Gwen Blum; gwen.blum@gmail.com
# Description: Office365 MailBox Usage Report
# Ref. https://support.riverbed.com/apis/steelscript/appfwk/tutorial.html#creating-app-framework-reports
#
# Changelog:
# 20160507 Gwen : add MailboxUsageTable - office365 mailbox usage report

# Copyright (c) 2015 Riverbed Technology, Inc.
#
# This software is licensed under the terms and conditions of the MIT License
# accompanying the software ("License").  This software is distributed "AS IS"
# as set forth in the License.


import logging
logger = logging.getLogger(__name__)

from steelscript.appfwk.apps.report.models import Report
report = Report.create("Office365 MailBox Usage Report")
report.add_section("Main")

from steelscript.appfwk.apps.datasource.models import Column, TableField
import steelscript.appfwk.apps.report.modules.yui3 as yui3

# Import the datasource module for this plugin
import steelscript.o365.appfwk.datasources.o365_source as o365

table = o365.O365MailboxUsageTable.create(name='O365MailboxUsage')
# OUTPUT example
# [...
# {'Date': '2016-05-03T00:00:00','TotalInactiveMailboxCount': '7','TotalMailboxCount': '12'}
# ... ]

# Report 
table.add_column('Date','Date', datatype='date',iskey=True)
table.add_column('TotalInactiveMailboxCount','Total Inactive Mailbox Count', datatype='integer')
table.add_column('TotalMailboxCount',label='Total Mailbox Count', datatype='integer')
report.add_widget(yui3.TableWidget, table, 'MailBox Usage Table', width=12)
report.add_widget(yui3.TimeSeriesWidget, table, 'Mailbox Usage Timeseries', width=12)