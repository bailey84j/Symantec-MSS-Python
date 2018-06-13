import requests
import string
from xml.etree import ElementTree

Pages = ["incidents", "organizations", "devices", "tickets"]
for Page in Pages:
    URL = "https://api.monitoredsecurity.com/SWS/" + Page + ".asmx?WSDL"
    WDSL = requests.get(url=URL)

    # WDSLxml = WDSL.Content

    # convert string with declaration back to xml
    root = ElementTree.fromstring(WDSL.content)

    print(ElementTree.tostring(root, encoding='utf-8', method='xml'))

    for child in root:
        print(child.tag)

    for element in root.findall('s:element'):
        print(element)
    # $WDSLxml.OuterXml | Out-File .\org.xml
    # $Elements = $WDSLxml.definitions.types.schema.element

    import xml.etree.ElementTree as ET

    tree = ElementTree.parse()
    root = tree.getroot()

    ns = {'s': "http://www.w3.org/2001/XMLSchema",
          'soap12': "http://schemas.xmlsoap.org/wsdl/soap12/",
          'http': "http://schemas.xmlsoap.org/wsdl/http/",
          'mime': "http://schemas.xmlsoap.org/wsdl/mime/",
          'tns': "https://www.monitoredsecurity.com/",
          'soap': "http://schemas.xmlsoap.org/wsdl/soap/",
          'tm': "http://microsoft.com/wsdl/mime/textMatching/",
          'soapenc': "http://schemas.xmlsoap.org/soap/encoding/",
          'wsdl': "http://schemas.xmlsoap.org/wsdl/"}

# root.findall("./{http://schemas.xmlsoap.org/wsdl/}types/{http://www.w3.org/2001/XMLSchema}schema/{http://www.w3.org/2001/XMLSchema}element")

for element in root.findall("./wsdl:types/s:schema/s:element", ns):
    function_str = 'def '
    # region get function name
    name = element.get('name')
    if 'Get' in name:
        function_name = 'GetMSS' + name.replace('Get', '')
        print(function_name);
    elif 'Create' in name:
        function_name = 'NewMSS' + name.replace('Create', '')
        print(function_name);
    elif 'Add' in name:
        function_name = 'AddMSS' + name.replace('Add', '')
        print(function_name);
    elif 'Update' in name:
        function_name = 'UpdateMSS' + name.replace('Update', '')
        print(function_name);
    else:
        function_name = 'GetMSS' + name
        print(function_name);
    # endregion get function name
    function_str = function_str + function_name + '('

    # region certificate parameters
    function_str = function_str + 'certificatepath,certificatepassword,'
    # endregion certificate parameters

    # region get required parameters
    function_output = []
    for selement in root.findall("./wsdl:types/s:schema/s:element[@name='" + name + "']/s:complexType/s:sequence/s:element", ns):
        if selement.attrib['name'].lower() not in function_output:
            function_output.append(selement.attrib['name'].lower())
            if selement.attrib['minOccurs'] == 1:
                function_str = function_str + selement.attrib['name'].lower() + ','
            else:
                function_str = function_str + selement.attrib['name'].lower() + '=None,'

    #response Field
    response_output=[]
    for selement in root.findall("./wsdl:types/s:schema/s:element[@name='" + name + "Response']/s:complexType/s:sequence/s:element", ns):
        response = "./soap:Envelope.soap:Body" + name + "Response/" + selement.attrib['name'].lower()

    function_str = function_str[:-1]
    function_str = function_str + '):\n'
    # endregion get required parameters
    # function_str = function_str +
    # region function header - imports
    function_header = """
    from pycore import pfx_to_pem
    from xml.etree import ElementTree
    import MSSCore
    import requests
    import json
    import xmltodict
    
    """
    function_str = function_str + function_header
    # endregion function header - imports
    # region paramaters to xml

    # endregion paramaters to xml
    # region function main body
    function_body = """Header = MSSCore.NewMSSHeader(MSSAction='""" + name + """')
    Body = MSSCore.NewMSSBody(MSSAction='""" + name + """')
    Bodystr = ElementTree.tostring(Body, encoding='utf8', method='xml')
    SERVER_URL = 'https://api.monitoredsecurity.com/SWS/""" + Page + """.asmx'

    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        MSSActionResult = requests.post(SERVER_URL, cert=cert, data=Bodystr, headers=Header)

    jsonString = json.dumps(xmltodict.parse(MSSActionResult))
    #, indent=4)
    return jsonString"""

    function_str = function_str + function_body
    # endregion function main body

    break

f = open(function_name + ".py","w+")

#text_file = open("test-Output.py", "w")
f.write(function_str)
f.close()


