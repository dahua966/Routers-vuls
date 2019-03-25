#-*- coding:utf-8 -*-
#这个可以用
#import lib-file
import urllib
import socket
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer 
import argparse 

info = open("proxy3.txt","ab")
cgis = open("cgis.txt","ab")
paths = []
def loadinfo(text):
    info.write(text.encode("utf-8"))

def loadinfo0(text):
    cgis.write(text.encode("utf-8"))

#define handler function class
class MyHandler(BaseHTTPRequestHandler):
    #HTTP method GET (e.x.)
    def do_GET(self):
        url = self.path
        protocol,rest = urllib.splittype(url)
        host,path = urllib.splithost(rest)
        host,port = urllib.splitnport(host)
        port = 80 if port < 0 else port
        host_ip = socket.gethostbyname(host)
        del self.headers['Proxy-Connection']

        self.headers['Connection'] = 'close'

        send_data = 'GET ' + path + ' HTTP/1.1' + '\r\n'
        head = ''
        for key, val in self.headers.items():
            head = head + "%s: %s\r\n" % (key, val)
        send_data = send_data + head + '\r\n'
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        block = ['.png','.css','.jpg','.gif','.js']
        bb = True
        for b in block:
            if b in path:
                bb = False
                break
        
        client.connect((host_ip,port))
        client.send(send_data)
        data = ''
        while True:
            tmp = client.recv(4096)
            if not tmp:
                break
            data = data + tmp
        if 'top.location.href = "/dir_login.asp"' in data:
            data = data.replace('top.location.href = "/dir_login.asp"','')
        if bb and path not in paths:
            # loadinfo(send_data)
            # loadinfo0(path+"\r\n")
            paths.append(path)
            print(send_data)
            print(data+"\r\n\r\n")
        client.close()
        self.wfile.write(data)

    #HTTP method POST (e.x.)
    def do_POST(self):
        url = self.path
        protocol,rest = urllib.splittype(url)
        host,path = urllib.splithost(rest)
        host,port = urllib.splitnport(host)
        port = 80 if port < 0 else port
        host_ip = socket.gethostbyname(host)
        datas = self.rfile.read(int(self.headers['content-length']))
        datas = urllib.unquote(datas).decode("utf-8", 'ignore')
        del self.headers['Proxy-Connection']
        self.headers['Connection'] = 'close'

        send_data = 'POST ' + path + ' HTTP/1.1' + '\r\n'
        head = ''
        for key, val in self.headers.items():
            head = head + "%s: %s\r\n" % (key, val)
        send_data = send_data + head + '\r\n'
        send_data = send_data + "\r\n" +datas
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((host_ip,port))

        print(send_data)
        client.send(send_data)
        
        data = ''
        while True:
            tmp = client.recv(4096)
            if not tmp:
                break
            data = data + tmp
        if 'top.location.href = "/dir_login.asp"' in data:
            data = data.replace('top.location.href = "/dir_login.asp"','')
        print(data + "\r\n\r\n")
        client.close()
        self.wfile.write(data)

def main():
    try:
        server = HTTPServer(('127.0.0.1', 8888), MyHandler)
        print 'listening on 8888...'
        server.serve_forever()
        print "test end"
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        info.close()
        server.socket.close()

if __name__ == '__main__':
    main()