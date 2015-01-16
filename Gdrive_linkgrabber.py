import urllib2, sys

FROM = "/d/"
TO = "/view"
DLINK = "http://drive.google.com/uc?export=view&id="

def getFileID(url):
    try:
        start = url.index(FROM) + len(FROM)
        end = url.index(TO,start)
        return url[start:end]
    except ValueError:
        print "Error"
        sys.exit(0)
       
def getDirectLink(fileID):
    org_link = DLINK + fileID
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(org_link)
    directed_url = request.url
    return directed_url, org_link

url = raw_input("Enter the file URL on Google Drive: ")
fileID = getFileID(url)
direct_link, semi_direct_link = getDirectLink(fileID)

print "Full direct link:\n%s" %direct_link
print "Semi-dierct link:\n%s" %semi_direct_link
