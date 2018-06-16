

def getmssticketcategories(certificatepath, certificatepassword):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetCategories')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetCategories', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetCategoriesResponse/ms:TicketGetCategoriesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        

def getmssticketcategories(certificatepath, certificatepassword):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetCategories')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetCategories', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetCategoriesResponse/ms:TicketGetCategoriesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetCategories')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetCategories', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetCategoriesResponse/ms:TicketGetCategoriesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdate')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdate')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdate', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateResponse/ms:TicketUpdateResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdate')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdate')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdate', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateResponse/ms:TicketUpdateResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdate')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdate')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdate', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateResponse/ms:TicketUpdateResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateRevised')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateRevised')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateRevised', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateRevisedResponse/ms:RequestCreateRevisedResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateRevised')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateRevised')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateRevised', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateRevisedResponse/ms:RequestCreateRevisedResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateRevised')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateRevised')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateRevised', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateRevisedResponse/ms:RequestCreateRevisedResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreate')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreate')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreate', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateResponse/ms:RequestCreateResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreate')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreate')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreate', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateResponse/ms:RequestCreateResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreate')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreate')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreate', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateResponse/ms:RequestCreateResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketQuery')
    body = MSSCore.NewMSSBody(MSSAction='TicketQuery')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketQuery', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketQueryResponse/ms:TicketQueryResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketQuery')
    body = MSSCore.NewMSSBody(MSSAction='TicketQuery')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketQuery', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketQueryResponse/ms:TicketQueryResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketQuery')
    body = MSSCore.NewMSSBody(MSSAction='TicketQuery')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketQuery', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketQueryResponse/ms:TicketQueryResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='RequestGetCategories')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestGetCategories', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestGetCategoriesResponse/ms:RequestGetCategoriesResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='RequestGetCategories')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestGetCategories', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestGetCategoriesResponse/ms:RequestGetCategoriesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestGetCategories')
    body = MSSCore.NewMSSBody(MSSAction='RequestGetCategories')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestGetCategories', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestGetCategoriesResponse/ms:RequestGetCategoriesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetStatuses')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetStatuses')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetStatuses', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetStatusesResponse/ms:TicketGetStatusesResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetStatuses')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetStatuses')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetStatuses', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetStatusesResponse/ms:TicketGetStatusesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetStatuses')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetStatuses')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetStatuses', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetStatusesResponse/ms:TicketGetStatusesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetUrgencies')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetUrgencies')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetUrgencies', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetUrgenciesResponse/ms:TicketGetUrgenciesResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetUrgencies')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetUrgencies')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetUrgencies', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetUrgenciesResponse/ms:TicketGetUrgenciesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetUrgencies')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetUrgencies')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetUrgencies', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetUrgenciesResponse/ms:TicketGetUrgenciesResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetList', ns) 
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetListResponse/ms:TicketGetListResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetList', ns) 
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetListResponse/ms:TicketGetListResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetList', ns) 
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetListResponse/ms:TicketGetListResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachments')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachments')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateWithAttachments', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsResponse/ms:RequestCreateWithAttachmentsResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachments')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachments')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateWithAttachments', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsResponse/ms:RequestCreateWithAttachmentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachments')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachments')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateWithAttachments', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsResponse/ms:RequestCreateWithAttachmentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetAttachmentList', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentListResponse/ms:TicketGetAttachmentListResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetAttachmentList', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentListResponse/ms:TicketGetAttachmentListResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetAttachmentList', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentListResponse/ms:TicketGetAttachmentListResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentContents')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentContents')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetAttachmentContents', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if attachmentitemoid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentItemOID')
        new_dec.text = attachmentitemoid 
    if isallattachmentsrequried != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'IsAllAttachmentsRequried')
        new_dec.text = isallattachmentsrequried
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentContentsResponse/ms:TicketGetAttachmentContentsResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentContents')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentContents')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetAttachmentContents', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if attachmentitemoid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentItemOID')
        new_dec.text = attachmentitemoid 
    if isallattachmentsrequried != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'IsAllAttachmentsRequried')
        new_dec.text = isallattachmentsrequried
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentContentsResponse/ms:TicketGetAttachmentContentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetAttachmentContents')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetAttachmentContents')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetAttachmentContents', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if attachmentitemoid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentItemOID')
        new_dec.text = attachmentitemoid 
    if isallattachmentsrequried != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'IsAllAttachmentsRequried')
        new_dec.text = isallattachmentsrequried
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketGetAttachmentContentsResponse/ms:TicketGetAttachmentContentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if attachmentitemoid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentItemOID')
        new_dec.text = attachmentitemoid 
    if isallattachmentsrequried != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'IsAllAttachmentsRequried')
        new_dec.text = isallattachmentsrequried
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketDeleteAttachments')
    body = MSSCore.NewMSSBody(MSSAction='TicketDeleteAttachments')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketDeleteAttachments', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ticketID')
        new_dec.text = ticketid 
    if attachmentoidlist != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'attachmentOIDList')
        new_dec.text = attachmentoidlist 
    if updatecomment != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'updateComment')
        new_dec.text = updatecomment 
    if retryattempts != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'retryAttempts')
        new_dec.text = retryattempts
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketDeleteAttachmentsResponse/ms:TicketDeleteAttachmentsResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketDeleteAttachments')
    body = MSSCore.NewMSSBody(MSSAction='TicketDeleteAttachments')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketDeleteAttachments', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ticketID')
        new_dec.text = ticketid 
    if attachmentoidlist != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'attachmentOIDList')
        new_dec.text = attachmentoidlist 
    if updatecomment != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'updateComment')
        new_dec.text = updatecomment 
    if retryattempts != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'retryAttempts')
        new_dec.text = retryattempts
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketDeleteAttachmentsResponse/ms:TicketDeleteAttachmentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketDeleteAttachments')
    body = MSSCore.NewMSSBody(MSSAction='TicketDeleteAttachments')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketDeleteAttachments', ns) 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ticketID')
        new_dec.text = ticketid 
    if attachmentoidlist != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'attachmentOIDList')
        new_dec.text = attachmentoidlist 
    if updatecomment != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'updateComment')
        new_dec.text = updatecomment 
    if retryattempts != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'retryAttempts')
        new_dec.text = retryattempts
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketDeleteAttachmentsResponse/ms:TicketDeleteAttachmentsResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ticketID')
        new_dec.text = ticketid 
    if attachmentoidlist != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'attachmentOIDList')
        new_dec.text = attachmentoidlist 
    if updatecomment != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'updateComment')
        new_dec.text = updatecomment 
    if retryattempts != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'retryAttempts')
        new_dec.text = retryattempts
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachment')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachment')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachment', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentResponse/ms:TicketUpdateWithAttachmentResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachment')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachment')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachment', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentResponse/ms:TicketUpdateWithAttachmentResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachment')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachment')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachment', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentResponse/ms:TicketUpdateWithAttachmentResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentRevised')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentRevised')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachmentRevised', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentRevisedResponse/ms:TicketUpdateWithAttachmentRevisedResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentRevised')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentRevised')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachmentRevised', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentRevisedResponse/ms:TicketUpdateWithAttachmentRevisedResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentRevised')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentRevised')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachmentRevised', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentRevisedResponse/ms:TicketUpdateWithAttachmentRevisedResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetRecentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetRecentList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetRecentList', ns) 
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
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
        

def getmssticketrecentlist(certificatepath, certificatepassword, status=None, ticketcategory=None, urgency=None, ticketid=None, clientreference=None, device=None, requestedbyorganization=None, assignedtoorganization=None, maxtickets=None, starttimestampgmt=None, endtimestampgmt=None):

    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict 
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetRecentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetRecentList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetRecentList', ns) 
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketGetRecentList')
    body = MSSCore.NewMSSBody(MSSAction='TicketGetRecentList')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketGetRecentList', ns) 
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
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
         
    if status != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Status')
        new_dec.text = status 
    if ticketcategory != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketCategory')
        new_dec.text = ticketcategory 
    if urgency != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Urgency')
        new_dec.text = urgency 
    if ticketid != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketID')
        new_dec.text = ticketid 
    if clientreference != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'ClientReference')
        new_dec.text = clientreference 
    if device != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Device')
        new_dec.text = device 
    if requestedbyorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestedByOrganization')
        new_dec.text = requestedbyorganization 
    if assignedtoorganization != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AssignedToOrganization')
        new_dec.text = assignedtoorganization 
    if maxtickets != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'MaxTickets')
        new_dec.text = maxtickets 
    if starttimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'StartTimeStampGMT')
        new_dec.text = starttimestampgmt 
    if endtimestampgmt != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'EndTimeStampGMT')
        new_dec.text = endtimestampgmt
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachmentsExt')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachmentsExt')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateWithAttachmentsExt', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsExtResponse/ms:RequestCreateWithAttachmentsExtResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachmentsExt')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachmentsExt')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateWithAttachmentsExt', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsExtResponse/ms:RequestCreateWithAttachmentsExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='RequestCreateWithAttachmentsExt')
    body = MSSCore.NewMSSBody(MSSAction='RequestCreateWithAttachmentsExt')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/RequestCreateWithAttachmentsExt', ns) 
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:RequestCreateWithAttachmentsExtResponse/ms:RequestCreateWithAttachmentsExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if requestcreatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestCreateDoc')
        new_dec.text = requestcreatedoc 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentExt')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentExt')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachmentExt', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentExtResponse/ms:TicketUpdateWithAttachmentExtResult', ns)
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentExt')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentExt')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachmentExt', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentExtResponse/ms:TicketUpdateWithAttachmentExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='TicketUpdateWithAttachmentExt')
    body = MSSCore.NewMSSBody(MSSAction='TicketUpdateWithAttachmentExt')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/TicketUpdateWithAttachmentExt', ns) 
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentExtResponse/ms:TicketUpdateWithAttachmentExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
         
    if ticketupdatedoc != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'TicketUpdateDoc')
        new_dec.text = ticketupdatedoc 
    if requesttoclose != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'RequestToClose')
        new_dec.text = requesttoclose 
    if attachments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'Attachments')
        new_dec.text = attachments 
    if attachmentcomments != "":
        new_dec = ElementTree.SubElement(body_variable_section, 'AttachmentComments')
        new_dec.text = attachmentcomments
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
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
        
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='ArrayOfAttachment')
    body = MSSCore.NewMSSBody(MSSAction='ArrayOfAttachment')
    mss_url = 'https://api.monitoredsecurity.com/SWS/tickets.asmx'
    body_variable_section = body.find('./soap:Body/ArrayOfAttachment', ns)
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('./soap:Body/ms:TicketUpdateWithAttachmentExtResponse/ms:TicketUpdateWithAttachmentExtResult', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        