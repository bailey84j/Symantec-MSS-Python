def NewMSSBody(MSSAction=None):
    from xml.etree import ElementTree
    # region NameSpace Variables
    xsi_ns = "http://www.w3.org/2001/XMLSchema-instance"
    xsd_ns = "http://www.w3.org/2001/XMLSchema"
    soap12_ns = "http://www.w3.org/2003/05/soap-envelope"
    mss_ns = "https://www.monitoredsecurity.com/"
    # endregion NameSpace Variables
    # region Register NameSpaces
    ElementTree.register_namespace("soap12", soap12_ns)
    ElementTree.register_namespace("xsd", xsd_ns)
    ElementTree.register_namespace("xsi", xsi_ns)
    ElementTree.register_namespace("", mss_ns)
    # endregion Register NameSpaces
    # region create soap12:envelope node
    soapenvelopexmlnode = ElementTree.QName(soap12_ns, "Envelope")     # Element QName
    soapenvelopexmlnode = ElementTree.Element(ElementTree.QName(soap12_ns, "Envelope"))
    # region add extra namespace attributes
    soapenvelopexmlnode.set('xmlns:xsi', xsi_ns)
    soapenvelopexmlnode.set('xmlns:xsd', xsd_ns)
    # endregion add extra namespace attributes
    # endregion create soap12:envelope node
    # region create soap12:body node
    soapbodyxmlnode = ElementTree.Element(ElementTree.QName(soap12_ns, "Body"))
    # endregion create soap12:body node
    # region add soap12:body node to soap12:envelope node
    soapenvelopexmlnode.append(soapbodyxmlnode)
    # endregion add soap12:body node to soap12:envelope node
    # region create Action node
    mssactionxmlnode = ElementTree.Element(ElementTree.QName(MSSAction))
    mssactionxmlnode.set('xmlns', mss_ns)
    # endregion create Action node
    # region add Action Node to soap12:body node
    soapbodyxmlnode.append(mssactionxmlnode)
    # region add Action Node to soap12:body node
    #print(ElementTree.tostring(soapenvelopexmlnode, encoding='utf-8', method='xml'))
    # endregion add Action Node to soap12:body node
    return soapenvelopexmlnode

