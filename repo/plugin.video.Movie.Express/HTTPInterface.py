import urllib, re
import xbmc,xbmcgui
import time
import urllib2
import shutil
import urlparse
import os
import os.path
import hashlib

from t0mm0.common.net import Net

def http_get(url, username='', password =''):
    form_data = {}
    form_data['username'] = 'gobihun'
    form_data['password'] = hashlib.md5('pihacker').hexdigest()[10:18]
    login_url = "http://www.einthusan.com/etc/login.php"
    http_post(login_url, postData=form_data)
    try:
        return Net().http_GET(url).content
    except urllib2.URLError, e:
        xbmcgui.Dialog().ok(ADDON.getAddonInfo('name'), 'Unable to connect to website', '', '') 
        return ""

def http_post(url, postData={}, data=''):
    try:
        if (data != ''):
            postData = dict(urlparse.parse_qsl(data))
        return Net().http_POST(url, postData).content
    except urllib2.URLError, e:
        xbmcgui.Dialog().ok(ADDON.getAddonInfo('name'), 'Unable to login to website', '', '') 
        return ""
