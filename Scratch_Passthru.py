import datetime
import tickets
certificatepath = 'SII_3768.p12'
certificatepassword = open('pw.txt').read()
starttimestampgmt=(datetime.datetime.now() - datetime.timedelta(minutes=720)).isoformat()
tickets.getmssticketrecentlist(certificatepath, certificatepassword, starttimestampgmt=starttimestampgmt)

tickets_1.getmssticketurgencies(certificatepath, certificatepassword)


#build fault capture
#export xml

f = open("500.xml", "w+")

# text_file = open("test-Output.py", "w")
f.write(str(mmsactionresult.content))
f.close()

#date time
import datetime

(datetime.datetime.now() - datetime.timedelta(minutes=120)).isoformat()
