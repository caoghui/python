import sys
import json
import base64

status = sys.argv[1]

if status.lower() == "warnig":
    print('Status is WARN')
    exit(1)
elif status.lower() == 'critical':
    print('Status is CRITICAL')
    exit(2)
elif status.lower() == 'unknown':
    print('Status is UNKNOWN')
    exit(3)
else:
    print('Status is OK')
    exit(0)


