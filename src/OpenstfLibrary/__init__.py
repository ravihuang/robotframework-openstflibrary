#  Copyright (c) 2010 Franz Allan Valencia See
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from robot.api import logger
import os,time,logging
try:
    import urlparse
except:
    import urllib.parse
from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose

__version__ = '0.1.1'


class OpenstfLibrary:
    """
    Openstf Library contains utilities meant for Robot Framework's usage.
    This can allow you to stub a interface for your client test
    References:
     + abc - http://
    Notes:
    `compatible* - or at least theoretically it should be compatible. Currently tested only with win7`
    Example Usage:
    | connect to stf | localhost | token
    | ${x} | get idle device
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'    
    def __init__(self):
        self.set_swagger_log_level(logging.WARN)

    def set_swagger_log_level(self,level):
        logging.getLogger("pyswagger.core").setLevel(int(level))

    def connect_to_stf(self,host,token):
        self.app = App._create_('http://%s/api/v1/swagger.json' % host)
        auth = Security(self.app)
        auth.update_with('accessTokenAuth', 'Bearer '+token)
        self.client = Client(auth)
    
    def get_user_name(self):
        user=self.__req('getUser') 
        if not (user and user['success']):
            return None
        return user['user']['name']
    
    def get_user_devices(self):
        rst=self.__req('getUserDevices')     
        if not(rst['success'] and rst['devices']):
            return None    
        return rst['devices']
    def __req(self,op):
        req, resp = self.app.op[op]()
        loop=5
        while True and loop:
            rst=self.client.request((req, resp))
            rst=rst.data
            if rst['success']:
                logger.debug(rst)
                return rst
            time.sleep(3)   
            loop-=1
        return None
    def get_idle_device(self):
        rst=self.__req('getDevices')
        for i in rst['devices']:
            if i['using']:
                continue
            return i['serial']
        return None  
