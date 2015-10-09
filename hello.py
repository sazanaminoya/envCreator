# coding: utf-8

strFile =  "sample.txt"
vFile = open(strFile, 'r')
linNo = 0
for line in vFile.readlines():
    if line.find("forwarded_port") >= 0:
        break
    linNo += 1

vFile.close()

vFile = open(strFile, 'w')

tempNo = 0
for line in vFile.readlines():
    if tempNo ==  linNo:
        vFile.write(all)
        vFile.write("config.vm.network \"forwarded_port\", guest: 3000, host: 3000")
        vFile.write("config.vm.network \"forwarded_port\", guest: 4567, host: 4567")
        break
    tempNo += 1
