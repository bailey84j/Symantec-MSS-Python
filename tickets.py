

def getmssticketcategories(certificatepath, certificatepassword):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetCategories')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetCategoriesResponse/ms:TicketGetCategoriesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def updatemssticket(certificatepath, certificatepassword, ticketupdatedoc=None, requesttoclose=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdate')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdate')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateResponse/ms:TicketUpdateResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def newmssrequestrevised(certificatepath, certificatepassword, requestcreatedoc=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateRevised')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateRevised')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateRevisedResponse/ms:RequestCreateRevisedResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def newmssrequest(certificatepath, certificatepassword, requestcreatedoc=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreate')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreate')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateResponse/ms:RequestCreateResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketquery(certificatepath, certificatepassword, ticketid=None, clientreference=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketQuery')
    body = MSSCore.NewMSSBody(MSSAction='TicketQuery')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketQueryResponse/ms:TicketQueryResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssrequestcategories(certificatepath, certificatepassword):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='RequestGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='RequestGetCategories')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestGetCategoriesResponse/ms:RequestGetCategoriesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketstatuses(certificatepath, certificatepassword):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetStatuses')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetStatuses')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetStatusesResponse/ms:TicketGetStatusesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketurgencies(certificatepath, certificatepassword):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetUrgencies')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetUrgencies')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetUrgenciesResponse/ms:TicketGetUrgenciesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketlist(certificatepath, certificatepassword, status=None, ticketcategory=None, urgency=None, ticketid=None, clientreference=None, device=None, requestedbyorganization=None, assignedtoorganization=None, maxtickets=None, starttimestampgmt=None, endtimestampgmt=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetList')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetListResponse/ms:TicketGetListResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def newmssrequestwithattachments(certificatepath, certificatepassword, requestcreatedoc=None, attachments=None, attachmentcomments=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachments')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachments')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsResponse/ms:RequestCreateWithAttachmentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketattachmentlist(certificatepath, certificatepassword, ticketid=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentList')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentListResponse/ms:TicketGetAttachmentListResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketattachmentcontents(certificatepath, certificatepassword, ticketid=None, attachmentitemoid=None, isallattachmentsrequried=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentContents')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentContents')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentContentsResponse/ms:TicketGetAttachmentContentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketdeleteattachments(certificatepath, certificatepassword, ticketid=None, attachmentoidlist=None, updatecomment=None, retryattempts=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketDeleteAttachments')
    body = MSSCore.NewMSSBody(MSSAction='TicketDeleteAttachments')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketDeleteAttachmentsResponse/ms:TicketDeleteAttachmentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def updatemssticketwithattachment(certificatepath, certificatepassword, ticketupdatedoc=None, requesttoclose=None, attachments=None, attachmentcomments=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachment')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachment')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentResponse/ms:TicketUpdateWithAttachmentResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def updatemssticketwithattachmentrevised(certificatepath, certificatepassword, ticketupdatedoc=None, requesttoclose=None, attachments=None, attachmentcomments=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentRevised')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentRevised')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentRevisedResponse/ms:TicketUpdateWithAttachmentRevisedResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketrecentlist(certificatepath, certificatepassword, status=None, ticketcategory=None, urgency=None, ticketid=None, clientreference=None, device=None, requestedbyorganization=None, assignedtoorganization=None, maxtickets=None, starttimestampgmt=None, endtimestampgmt=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetRecentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetRecentList')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'

    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")

    # region NameSpace Variables
    xsi_ns = "http://www.w3.org/2001/XMLSchema-instance"
    xsd_ns = "http://www.w3.org/2001/XMLSchema"
    soap12_ns = "http://www.w3.org/2003/05/soap-envelope"
    mss_ns = "https://www.monitoredsecurity.com/"
    # endregion NameSpace Variables

    starttimestampgmt = "date"

    body_variable_section = body.find('./soap:Body/TicketGetRecentList', ns).text
    # region add soap12:body node to soap12:envelope node
    variablexmlnode = ElementTree.Element(ElementTree.QName(starttimestampgmt))
    variablexmlnode.text = 'Dat1'
    ElementTree.tostring(variablexmlnode)
    # region add Action Node to soap12:body node
    t.append(variablexmlnode)
    ElementTree.tostring(body)
    eve = ElementTree.Element("soap12:Envelope")
    t = ElementTree.SubElement(eve,'soap12:Body')
    body    # region add Action Node to soap12:body node


    ElementTree.dump(body)

    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    

    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetRecentListResponse/ms:TicketGetRecentListResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def newmssrequestwithattachmentsext(certificatepath, certificatepassword, requestcreatedoc=None, attachments=None, attachmentcomments=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachmentsExt')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachmentsExt')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsExtResponse/ms:RequestCreateWithAttachmentsExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def updatemssticketwithattachmentext(certificatepath, certificatepassword, ticketupdatedoc=None, requesttoclose=None, attachments=None, attachmentcomments=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentExt')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentExt')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentExtResponse/ms:TicketUpdateWithAttachmentExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssarrayofattachment(certificatepath, certificatepassword):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    header = MSSCore.NewMSSHeader(MSSAction='ArrayOfAttachment')
    body = MSSCore.NewMSSBody(MSSAction='ArrayOfAttachment')
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentExtResponse/ms:TicketUpdateWithAttachmentExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        