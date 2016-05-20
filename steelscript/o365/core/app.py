# steelscript/o365/core/app.py
# Version: 20160507 V04
# Author: Gwen Blum; gwen.blum@gmail.com
# Description: Office 365 Application Framework Plugin API
# Ref. https://support.riverbed.com/apis/steelscript/appfwk/tutorial.html
# Ref. https://docs.python.org/2/library/xml.etree.elementtree.html
#
# Changelog:
# 20160507 Gwen : add MailboxUsageTable - office365 mailbox usage report

import o365_settings

###############################
#### Mailbox Usage - EXAMPLE / TEST with static data
###############################

def get_MailBoxUsage_TEST(userid,password, begin, end):
	"""
	Get Office365 MailBoxUsage TEST with static data
	"""
	return [{'Date': '2016-04-05', 'TotalInactiveMailboxCount': '8', 'TotalMailboxCount': '12'}, {'Date': '2016-04-06', 'TotalInactiveMailboxCount': '8', 'TotalMailboxCount': '12'}, {'Date': '2016-04-07', 'TotalInactiveMailboxCount': '8', 'TotalMailboxCount': '12'}, {'Date': '2016-04-08', 'TotalInactiveMailboxCount': '8', 'TotalMailboxCount': '12'}, {'Date': '2016-04-09', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}, {'Date': '2016-04-10', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}, {'Date': '2016-04-11', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}, {'Date': '2016-04-12', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}, {'Date': '2016-04-13', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}]

   
###############################
#### Mailbox Usage
###############################


def get_MailBoxUsage(userid,password, begin, end):
    """
    Get Office365 MailBoxUsage
    """
    from pyslet.http.auth import BasicCredentials
    from pyslet.rfc2396 import URI
    credentials = BasicCredentials()
    credentials.userid = userid 
    credentials.password = password
    
    if credentials.userid == "":    
        credentials.userid = o365_settings.o365defaultuserid
    if credentials.password == "":    
        credentials.password = o365_settings.o365defaultpassword
    
    credentials.protectionSpace = URI.from_octets("https://reports.office365.com/ecp/reportingwebservice/reporting.svc").get_canonical_root()
# DEBUG
# str(credentials)

    import pyslet.http.client as http
    c = http.Client()
    c.add_credentials(credentials)
    r = http.ClientRequest('https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MailboxUsage')
    c.process_request(r)
# DEBUG
# r.response.status
# print r.response.get_content_type()
# #>>> application/atom+xml; charset=utf-8; type=feed
# print r.response.entity_body.getvalue()
    import xml.etree.ElementTree as ET
    root = ET.fromstring(r.response.entity_body.getvalue())
    ns = {'d': 'http://schemas.microsoft.com/ado/2007/08/dataservices' ,
        'm': 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata' }
    ret = []    
    for entry in root.findall('.//m:properties',ns):
        date = entry.find('d:Date',ns).text
        TotalMailboxCount = entry.find('d:TotalMailboxCount',ns).text
        TotalInactiveMailboxCount  = entry.find('d:TotalInactiveMailboxCount',ns).text
# DEBUG
# print date,TotalMailboxCount,TotalInactiveMailboxCount
        result = { 'Date': date , 'TotalMailboxCount' : TotalMailboxCount, 'TotalInactiveMailboxCount' : TotalInactiveMailboxCount  }
        ret.append(result)
    c.close()
    return ret

#OUTPUT EXAMPLE
#
# [{'Date': '2016-04-05', 'TotalInactiveMailboxCount': '8', 'TotalMailboxCount': '12'}, {'Date': '2016-04-06', 'TotalInactiveMailboxCount': '8', 'TotalMailboxCount': '12'}, {'Date': '2016-04-07', 'TotalInactiveMailboxCount': '8', 'TotalMailboxCount': '12'}, {'Date': '2016-04-08', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}, {'Date': '2016-05-01', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}, {'Date': '2016-05-02', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}, {'Date': '2016-05-03', 'TotalInactiveMailboxCount': '7', 'TotalMailboxCount': '12'}]

