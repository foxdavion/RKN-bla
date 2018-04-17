#!/usr/bin/python
import pprint
import re
import os
from netaddr import *
new = []
f = open('/opt/blackhol/subnets.txt')
line = f.readline()
while line:
    ip = IPNetwork(line)
    subnets = list(ip.subnet(24))
    for sub in subnets:
        new.append(sub)
    line = f.readline()


for x in new:
    netaddress = str(IPNetwork(x).cidr)
    print netaddress
    c='echo "announce route {0} next-hop x.x.x.x community 65001:666" > /var/run/exabgp.cmd'.format(x)
    os.system(c)


thefile = open('/opt/blackhol/sub.txt', 'w')
for item in new:
  thefile.write("%s\n" % item)
