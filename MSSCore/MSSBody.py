def NewMSSBody(MSSAction=None):
    from xml.etree import ElementTree
    XSI_NS  =  "http://www.w3.org/2001/XMLSchema-instance"
    XSD_NS   =  "http://www.w3.org/2001/XMLSchema"
    SOAP12_NS = "http://www.w3.org/2003/05/soap-envelope"
    MSS_NS = "https://www.monitoredsecurity.com/"
    ElementTree.register_namespace("soap12", SOAP12_NS)
    ElementTree.register_namespace("xsd", XSD_NS)
    ElementTree.register_namespace("xsi", XSI_NS)
    ElementTree.register_namespace("", MSS_NS)
    SoapEnvelopeXMLNode = ElementTree.QName(SOAP12_NS, "Envelope")     # Element QName
    SoapEnvelopeXMLNode = ElementTree.Element(ElementTree.QName(SOAP12_NS, "Envelope"))
    SoapEnvelopeXMLNode.set('xmlns:xsi',XSI_NS)
    SoapEnvelopeXMLNode.set('xmlns:xsd',XSD_NS)
    SoapBodyXMLNode = ElementTree.Element(ElementTree.QName(SOAP12_NS, "Body"))
    SoapEnvelopeXMLNode.append(SoapBodyXMLNode)
    MSSActionXMLNode = ElementTree.Element(ElementTree.QName(MSSAction))
    MSSActionXMLNode.set('xmlns',MSS_NS)
    SoapBodyXMLNode.append(MSSActionXMLNode)
    print(ElementTree.tostring(SoapEnvelopeXMLNode, encoding='utf-8', method='xml'))
    return SoapEnvelopeXMLNode

