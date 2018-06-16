import requests
import string
from xml.etree import ElementTree

Pages = ["incidents", "organizations", "devices", "tickets"]
for Page in Pages:
    URL = "https://api.monitoredsecurity.com/SWS/" + Page + ".asmx?WSDL"
    WDSL = requests.get(url=URL)

    page_str = ""

    # WDSLxml = WDSL.Content

    # convert string with declaration back to xml
    root = ElementTree.fromstring(WDSL.content)

    # print(ElementTree.tostring(root, encoding='utf-8', method='xml'))

    # for child in root:
    #    print(child.tag)

    # for element in root.findall('s:element'):
    #    print(element)
    # $WDSLxml.OuterXml | Out-File .\org.xml
    # $Elements = $WDSLxml.definitions.types.schema.element

    import xml.etree.ElementTree as ET

    # tree = ElementTree.parse()
    # root = tree.getroot()

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

    # region get function name
    name = element.get('name')
    if 'Response' not in name:
        function_str = 'def '
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
        function_str = function_str + function_name.lower() + '('

        # region certificate parameters
        function_str = function_str + 'certificatepath, certificatepassword, '
        # endregion certificate parameters

        # region get required parameters
        function_output = []
        function_var_to_xml = ""
        for selement in root.findall(
                "./wsdl:types/s:schema/s:element[@name='" + name + "']/s:complexType/s:sequence/s:element", ns):
            if selement.attrib['name'].lower() not in function_output:
                function_output.append(selement.attrib['name'].lower())
                if selement.attrib['minOccurs'] == 1:
                    function_str = function_str + selement.attrib['name'].lower() + ', '
                    function_var_to_xml = function_var_to_xml + """ 
    new_dec = ElementTree.SubElement(body_variable_section, '""" + selement.attrib['name'].lower() + """')
    new_dec.text = """ + selement.attrib['name'].lower()

                else:
                    function_str = function_str + selement.attrib['name'].lower() + '=None, '
                    function_var_to_xml = function_var_to_xml + """ 
    if """ + selement.attrib['name'].lower() + """ != "":
        new_dec = ElementTree.SubElement(body_variable_section, '""" + selement.attrib['name'] + """')
        new_dec.text = """ + selement.attrib['name'].lower()

        # response Field
        response_output = []
        for selement in root.findall(
                "./wsdl:types/s:schema/s:element[@name='" + name + "Response']/s:complexType/s:sequence/s:element", ns):
            response = "./soap:Body/ms:" + name + "Response/ms:" + selement.attrib['name']

        function_str = function_str[:-2]
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
        function_body = """
    ns = dict(soap="http://www.w3.org/2003/05/soap-envelope", xsi="http://www.w3.org/2001/XMLSchema-instance",
          xsd="http://www.w3.org/2001/XMLSchema", ms="https://www.monitoredsecurity.com/")
    
    header = MSSCore.NewMSSHeader(MSSAction='""" + name + """')
    body = MSSCore.NewMSSBody(MSSAction='""" + name + """')
    mss_url = 'https://api.monitoredsecurity.com/SWS/""" + Page + """.asmx'
    body_variable_section = body.find('./soap:Body/""" + name + """', ns)"""

    function_body = function_body + function_var_to_xml
    function_body = function_body + """
    body_str = ElementTree.tostring(body, encoding='utf8', method='xml')
    print (body_str)
    with pfx_to_pem(certificatepath, certificatepassword) as cert:
        mssactionresult = requests.post(mss_url, cert=cert, data=body_str, headers=header)
    
    root = ElementTree.fromstring(mssactionresult.content)
    
    if mssactionresult.status_code != 200:
        result = root.findall('./soap:Body/soap:Fault/detail/faultstring', ns)
    else:
        result = root.findall('""" + response + """', ns)
    print(ElementTree.tostring(result[0], encoding='utf-8', method='xml'))
    json_str = json.dumps(xmltodict.parse(ElementTree.tostring(result[0], encoding='utf-8', method='xml')))
    return json_str
        """

    function_str = function_str + function_body
    # endregion function main body

        page_str = page_str + "\n\n" + function_str
    else:
        function_str = ""

f = open(Page + ".py", "w+")

# text_file = open("test-Output.py", "w")
f.write(page_str)
f.close()



