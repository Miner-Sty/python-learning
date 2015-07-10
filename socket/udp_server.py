#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a server example which send time to client.'
__author__='Miner'

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口：
s.bind(('127.0.0.1', 9999))
print 'Bind UDP on 9999....'
while True:
	#接收数据：
	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' %addr
	s.sendto('Hello, %s!' %data, addr)