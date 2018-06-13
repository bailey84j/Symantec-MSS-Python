def GetMSSTicketCategories(certificatepath,certificatepassword,ticketgetcategoriesresult=None,ticketupdatedoc=None,requesttoclose=None,ticketupdateresult=None,requestcreatedoc=None,requestcreaterevisedresult=None,requestcreateresult=None,ticketid=None,clientreference=None,ticketqueryresult=None,requestgetcategoriesresult=None,ticketgetstatusesresult=None,ticketgeturgenciesresult=None,status=None,ticketcategory=None,urgency=None,device=None,requestedbyorganization=None,assignedtoorganization=None,maxtickets=None,starttimestampgmt=None,endtimestampgmt=None,ticketgetlistresult=None,attachments=None,attachmentcomments=None,requestcreatewithattachmentsresult=None,ticketgetattachmentlistresult=None,attachmentitemoid=None,isallattachmentsrequried=None,ticketgetattachmentcontentsresult=None,attachmentoidlist=None,updatecomment=None,retryattempts=None,ticketdeleteattachmentsresult=None,ticketupdatewithattachmentresult=None,ticketupdatewithattachmentrevisedresult=None,ticketgetrecentlistresult=None,requestcreatewithattachmentsextresult=None,ticketupdatewithattachmentextresult=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict
    
    Header = MSSCore.NewMSSHeader(MSSAction='TicketGetCategories')
    Body = MSSCore.NewMSSBody(MSSAction='TicketGetCategories')
    Bodystr = ElementTree.tostring(Body, encoding='utf8', method='xml')
    SERVER_URL = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'

    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        MSSActionResult = requests.post(SERVER_URL, cert=cert, data=Bodystr, headers=Header)

    jsonString = json.dumps(xmltodict.parse(MSSActionResult.content))
    #, indent=4)
    return jsonString