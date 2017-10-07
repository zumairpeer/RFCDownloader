import sys
url_module = ''

# in python3.x, request is a submodule inside urllib
if sys.version_info[0] >= 3:
    from urllib import request
    url_module = request
# in python 2.x, urllib has no submodules
else:
    import urllib2
    url_module = urllib2

try:
    rfc_num = int(sys.argv[1])
except(IndexError, ValueError):
    print('Must give RFC number(integer) as first argument')
    sys.exit(2)

template_url = 'http://www.ietf.org/rfc/rfc{}.txt'

url = template_url.format(rfc_num)
rfc_open = url_module.urlopen(url)
rfc_raw = rfc_open.read()
rfc = rfc_raw.decode()
print(rfc)