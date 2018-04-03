import sys
import json
import http.client
import urllib.parse
import base64
import socket

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOWN = 3

server, port = sys.argv[1].split(":")
vhost = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

#print(server, port, vhost, username, password)
#exit(0)

conn = http.client.HTTPConnection(server, port)

path = "/api/aliveness-test/%s" %urllib.parse.quote(vhost, safe="")

print(path)
exit(0)

method = "GET"
credentials = base64.b64encode("%s:%s"%(username, password))



try:
    conn.request(method, path, "", {"Content-Type" : "application/json", "Authorization" : "Basic " + credentials})
except socket.error:
    print("CRITICAL: Could not connect to ", server, ":", port)
    exit(EXIT_CRITICAL)

response = conn.getresponse()

if response.status > 299:
    print("CRITICAL: Broker not alive: ", response.read())
    exit(EXIT_CRITICAL)

print("OK: Broker alive: ", response.read())
exit(EXIT_OK)


