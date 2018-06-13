def NewMSSHeader(MSSAction):
    headers = {
        "content-Type": "application/soap+xml; charset=utf-8",
        "SOAPAction": "https://www.monitoredsecurity.com/" + MSSAction
    }
    return headers