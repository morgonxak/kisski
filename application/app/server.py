#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import socket
from threading import Thread, Lock

import time

clientID = {}
fileName = "./1.txt"


def pinger():
    while True:
        threads = []
        troops = []
        for key, value in clientID:
            def ping():
                (conn, lock) = value
                with lock:
                    try:
                        conn.send(b'p')
                        conn.recv(1)
                    except socket.error:
                        troops.append(key)
            t = Thread(target=ping, daemon=True)
            threads.append(t)
        for t in threads:
            t.join()
        for k in troops:
            clientID.pop(k)
        time.sleep(10)


def client_thread(conn, addr):
    try:
        id = conn.recv(3)
        if id not in clientID.keys():
            clientID[id] = (conn, Lock())
    except socket.error:
        print("Error with:", addr)
        return


def init_server():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.bind(('0.0.0.0', 6960))
        except socket.error:
            print('Cannot bind address')
            return

        pinger_thread = Thread(target=pinger, daemon=True)
        pinger_thread.start()

        while True:
            try:
                sock.listen(1)
                conn, addr = sock.accept()
            except socket.error:
                print('Connection refused!')
                continue
            client_thr = Thread(target=lambda: client_thread(conn, addr), daemon=True)
            client_thr.start()
    except KeyboardInterrupt:
        sock.close()
        print('Interrupted')

init_server()
