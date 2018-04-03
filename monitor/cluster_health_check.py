import sys
import json
import base64
import socket
import http.client

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOWN = 3

server, port = sys.argv[1].split(":")
username = sys.argv[2]
password = sys.argv[3]

node_list = sys.argv[4].split(",")
mem_critical = int(sys.argv[5])
mem_warning = int(sys.argv[6])


conn = http.client.HTTPConnection(server, port)

path = "/api/nodes"
method = "GET"

credentials = base64.b64encode("%s:%s"%(username, password))

try:
    conn.request(method, path, "", {"Content-Type": "application/json", "Authorization": "Basic " + credentials})
except socket.error:
    print("UNKNOWN: Could not connect to", server, port)
    exit(EXIT_UNKNOWN)

response = conn.getresponse()
if response.status > 299:
    print("UNKNOWN: Unexpected API error : ", response.read())
    exit(EXIT_UNKNOWN)

response = json.loads(response.read())
for node in response:
    if node["name"] in node_list and node["running"] != False:
        node_list.remove(node["name"])

if len(node_list):
    print("WARNING: Cluster missing nodes : ", str(node_list))
    exit(EXIT_WARNING)

for node in response:
    if node["mem_used"] > mem_critical:
        print("CRITICAL: Node", node["name"], "memory usage is ", node["mem_used"])
        exit(EXIT_CRITICAL)
    elif node["mem_used"] > mem_warning:
        print("WARNING: Node", node["name"], "memory usage is", node["mem_used"])
        exit(EXIT_WARNING)

print("OK: ", len(response), "nodes. All memory usage below ", mem_warning)
exit(EXIT_OK)
