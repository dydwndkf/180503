import requests

'''
r = requests.get("https://goo.gl/nVLutc")
print(r.history)
for h in r.history:
    print (h.url)
print (r.url)
'''


def isSpam(content, spamLinkDomains, redirectionDepth):
    splitcontent = content.split(" ")
    for i in range(len(splitcontent)):
        if 'https://' in splitcontent[i]:
            linkcheck = splitcontent[i]
    r = requests.get(linkcheck)
    if len(r.history) < redirectionDepth:
        return False
    if str(spamLinkDomains[0]) in r.url:
        if len(r.history) == redirectionDepth:
            return True
        else:
            return False
    else:
        return False

print(isSpam("spam spam https://goo.gl/nVLutc", ["http://www.filekok.com"], 2))
#print(isSpam("spam spam http://go.microsoft.com/fwlink/?linkid=99104", ["https://support.office.com/en-us/article/HA100319991"], 2))
