import tickets
certificatepath = 'SII_3768.p12'
certificatepassword = open('pw.txt').read()
tickets.getmssticketrecentlist(certificatepath,certificatepassword)

tickets.getmssticketurgencies(certificatepath,certificatepassword)


#build fault capture
#export xml

f = open("500.xml", "w+")

# text_file = open("test-Output.py", "w")
f.write(str(mmsactionresult.content))
f.close()