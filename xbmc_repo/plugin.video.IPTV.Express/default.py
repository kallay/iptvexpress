# -*- coding: utf-8 -*-
# ver 2.5

import utils, httplib2, socks, httplib, logging, time    
import urllib, re
import xbmc,xbmcgui
import time
import urllib2
import shutil
import urlparse
import os
import os.path
import hashlib
import xbmcplugin
import xbmcaddon
import xbmcvfs
import string, sys, traceback, unicodedata, cookielib
import xml.dom.minidom, base64

os = str(utils.get_os())

if (os == 'OSX'):
    from os_mac import iptvex
elif (os == 'Linux'):
    from os_linux import iptvex
elif (os == 'win32'):
    from os_win import iptvex
else:
    from express import iptvex


a = iptvex()

xbmcplugin.setContent(int(sys.argv[1]), 'movies')
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_LABEL)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATE)
except:
    pass
try:
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_GENRE)
except:
    pass

params=a.get_params()

url=None
name=None
mode=None
iconimage=None
fanart=None
origurl=None
shareurl=None
thumb=None
guid=None
page=None
index=None
ref=None

try:
    url=urllib.unquote_plus(params["url"])
except:
    pass
try:
    name=urllib.unquote_plus(params["name"])
except:
    pass
try:
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass
try:
    fanart=urllib.unquote_plus(params["fanart"])
except:
    pass
try:
    origurl = urllib.unquote_plus( params['origurl'] )
except:
    pass
try:
    shareurl = urllib.unquote_plus( params['shareurl'] )
except:
    pass
try:
    thumb = urllib.unquote_plus( params['thumb'] )
except:
    pass
try:
    guid = urllib.unquote_plus( params['guid'] )
except:
    pass
try:
    mode = int( params['mode'] )
except:
    pass
try:
    page = int( params['page'] )
except:
    pass
try:
    index = int( params['index'] )
except:
    pass
try:
    ref = urllib.unquote_plus( params['ref'] ) 
except:
    pass

a.get_category(url, name, iconimage, fanart, origurl, shareurl, thumb, guid, mode, page, index, ref)

xbmcplugin.endOfDirectory(int(sys.argv[1]))