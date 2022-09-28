# Simple-Fault-Detector


### env.py - Example
Server/env.py could look like this:
```
sender = 'ed@outlook.com'
password = 'never-gonna'
receivers = (
    ['give@you.up', 'tony@stark-industries.com'],
    ['Rick Astley', 'Tony Stark'])

client_ip = "x.x.x.x" # Whatever the ip of your esp is

udp_log_path = "/home/ab/Heating/udp.log"
log_path = "/home/ab/Heating/server.log"

msg = """From: Heating <heating@gmail.com>
To: RECEIVERNAME <RECEIVERMAIL>
MIME-Version: 1.0
Content-type: text/html
Subject: Error

<h3There is an error with the heating!</h1>
<h4>Error occured on [[DATE]] at [[TIME]].</h3>
"""
```
