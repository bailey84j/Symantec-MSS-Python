import tickets
pfx = 'SII_3768.p12'
pw = open('pw.txt').read()
tickets.GetMSSTicketRecentList(pfx,pw)

tickets.GetMSSTicketUrgencies(pfx,pw)