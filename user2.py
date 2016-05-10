#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import numpy
import os
import time
import sys
import re


import subprocess #для запуска программ


ID = '124'
i=1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t = 0

cmdImgStrimer = './start.sh' # команда для запуска
cmdOpenVPN = 'sudo openvpn --config ../../../vpn/client-4.ovpn'
'''
cmdImgStrimer = 'ping yandex.ru' # команда для запуска
cmdOpenVPN = 'ping googl.com'
'''

iP=0# количество запущиных процессов

img_streamer=0
vpn_proc=0
##
pP=0
p2P=0

def runCMD():
	global img_streamer
	global vpn_proc
	ex=0

	print "runOK"
	
	PIPE = subprocess.PIPE
	p = subprocess.Popen(cmdImgStrimer, shell=True, stdin=PIPE, stdout=PIPE,stderr=subprocess.STDOUT, close_fds=True)
	p2 = subprocess.Popen(cmdOpenVPN, shell=True, stdin=PIPE, stdout=PIPE,stderr=subprocess.STDOUT, close_fds=True)
	return 1
		
print "Connect..."
while 1:
	while 1:
		try: sock.connect(('109.234.39.42', 6960))
		except socket.error:
			time.sleep(2)
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			###все ок соедени
			try: sock.send(ID)# id
			except socket.error:
				break
			
			data = sock.recv(1)
			print "принимаю значения"

			if data == '1':
				print "Запускаем VPN и стрим"
				print "запуск программ"
				runCMD() #Запуск стрим и VPN
				while data == '1':
					sock.setblocking(0)
					try:data=sock.recv(1)
					except socket.error:
						print "данных нет"
					else:
						s = img_streamer.stdout.readline()
						s2 = vpn_proc.stdout.readline()
						if not s: break
						if not s2: break
						print s,s2
						p2P=vpn_proc.pid
						pP=img_streamer.pid
				print "дошол"
				if p2P!=0 or pP!=0:
					print "закрываем программу"
					print str(p2P)+" "+str(pP)
					proc1 = "killall -s 9 mjpg_streamer"
					proc2 = "killall -s 9 openvpn"
					subprocess.Popen(proc1, shell = True)
					subprocess.Popen(proc2, shell = True)


			break	
	sock.close()








