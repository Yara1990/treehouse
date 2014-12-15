#!/usr/bin/python

import string
import sys
import urllib
import re
import xml.etree.ElementTree as ET

arg=sys.argv[1]
feed=arg.replace("itpc://", "http://")

nEp=0
nSec=0
section=""
course=""
description=""

try:
    f=urllib.urlopen(feed)
    s=f.read()
    episodes=dict()
    repo=list()
    raiz = ET.fromstring(s)
    for canal in raiz.iter('channel'):
        for item in canal.iter('item'):
            u=item.find('enclosure').get('url') #get video url
            u=u.replace('download.mp4?','download.mp4?hd=yes&') #replace the video URL for the HD one
            parts=u.split('/') #split url to assign course, section and episode
            course=parts[4]

            if (section != parts[5]):
                nEp=1
                nSec=nSec+1

            section=parts[5]
            description=parts[6]
            episodes['c']=course
            episodes['s']=format(nSec,"02d")+'-'+section
            episodes['d']=format(nSec,"02d")+format(nEp,"02d")+'-'+description+'.mp4'
            episodes['u']=u

            repo.append(episodes.copy())

            nEp=nEp+1
    for ep in repo:
        output='TREEHOUSE/'+ep['c']+'/'+ep['s']+'/'+ep['d']
        print 'curl --limit-rate 800K -L --create-dirs -o "'+output+'" "'+ep['u']+'"'

except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Value error"
except:
    print "Unexpected error:", sys.exc_info()[0]
