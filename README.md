# steelscript-o365
#####Author: Gwen Blum
#####Date: 20160520
Need to integrate Office365 metrics in Portal? Steelscript App Framework can help.
The O365 plugin is developed with Steelscript App Framework.
It retrieves Office365 reporting data (such as Mailbox Usage) and show them in tables and other timeseries widgets using the Steelscript App Framework.

### Roadmap

Version 1.0.0 provides the core of the plugin with Office365 Mailbox Usage data feed, datasource and reports.

Next versions would focus on functionnal extension to get others Office 365 usage reports such as Mail Traffic, Spam,... and would consist in:
- Implementing new data feed inside steelscript-o365 / steelscript / o365 / core / app.py 
- Creating new datasources inside steelscript-o365 / steelscript / o365 / appfwk / datasources / o365_source.py 
- Creating new reports scripts in the folder steelscript-o365 / steelscript / o365 / appfwk / reports / 

### How to use it?

- See more at: https://splash.riverbed.com/docs/DOC-5608#sthash.AsyHMXXQ.dpuf

### Steelscript App Framework (Riverbed)?

- https://github.com/riverbed
- https://support.riverbed.com/apis/steelscript/appfwk/toc.html
- ...


### Office365 reports Odata (Microsoft)?

- Office 365 Reporting web service: https://msdn.microsoft.com/en-us/library/office/jj984325.aspx
- https://technet.microsoft.com/en-us/library/dn781442.aspx
