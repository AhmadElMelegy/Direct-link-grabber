import sys, re, json, urllib2

def get_domain(url):
    DRIVE_INDICATOR = 'drive.google.com'
    DROPBOX_INDICATOR = 'dropbox.com'
    if DRIVE_INDICATOR in url:
        domain = "GD"
    elif DROPBOX_INDICATOR in url:
        domain = "DB"
    else:
        print "We currently deal with Google Drive and DropBox ONLY !"
        sys.exit(0)
    return domain

def get_gd_file_id(url):
    found = re.search('/d/(.+?)/view', url)
    if found:
        file_id = found.group(1)
        return file_id
    else:
         print "Error"
         sys.exit(0)
   
def get_gd_direct_link(file_id):
    DLINK = "https://drive.google.com/uc?export=view&id="
    org_link = DLINK + file_id
    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
    request = opener.open(org_link)
    direct_url = request.url
    return direct_url

def get_db_direct_link(url):
    direct_url = url.replace("www.dropbox.com","dl.dropbox.com")
    return direct_url

def shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    postdata = {'longUrl':url}
    headers = {'Content-Type':'application/json'}
    request = urllib2.Request(
        post_url,
        json.dumps(postdata),
        headers
    )
    result = urllib2.urlopen(request).read()
    short_url = json.loads(result)['id']
    return short_url

def generate_gd_result(url):
    file_id = get_gd_file_id(url)
    direct_link = get_gd_direct_link(file_id)
    short_url = shorten_url(direct_link)
    print "Direct link:\n %s" % direct_link
    print "Short URL: %s" % short_url

def generate_db_result(url):
    direct_link = get_db_direct_link(url)
    print "Direct link:\n %s" % direct_link    

url = raw_input("Enter URL of a file on Google Drive or DropBox: ")
domain = get_domain(url)

if domain == "GD":
    generate_gd_result(url)
elif domain == "DB":
    generate_db_result(url)