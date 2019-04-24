# -*- coding: utf-8 -*-
"""
[uptime.py]
Uptime since runing app

[Author]
Denis Solovyov

[About]
The time since the launch of the application

[Commands]
>>> .uptime
returns the time the bot has been running
"""

import datetime
class Plugin:
    def __init__(self):
        self.start_time = datetime.datetime.now()
        pass
    
    def time_request(self):
        """Return a string with uptime"""
        time_now = datetime.datetime.now()
        delta =  time_now - self.start_time
        if delta.days > 0:
            delta_string = delta.strftime("%d %H:%M:%S")
        else:
            delta_string = delta.strftime("%H:%M:%S")
        return delta_string
        
    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.uptime':
                methods['send'](info['address'], Plugin.time_request(self))
        except Exception as e:
            print('error uptime plugin', e)
