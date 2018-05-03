import requests

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

