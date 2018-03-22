from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose
import logging,time
logging.basicConfig()
logger=logging.getLogger('stf')
logger.setLevel(logging.DEBUG)
def connect_to_stf(host,token):
    global app,client
    app = App._create_('http://%s/api/v1/swagger.json' % host)
    auth = Security(app)
    auth.update_with('accessTokenAuth', 'Bearer '+token)
    client = Client(auth)

def get_user_name():
    req, resp = app.op['getUser']()
    user = client.request((req, resp)).data
    logger.debug(user)
    if not (user and user['success']):
        return None
    return user['user']['name']

def get_user_devices():
    rst=__req('getUserDevices')     
    if not(rst['success'] and rst['devices']):
        return None    
    return rst['devices']
def __req(op):
    req, resp = app.op[op]()
    loop=5
    while True and loop:
        rst=client.request((req, resp))
        rst=rst.data
        if rst['success']:
            logger.debug(rst)
            return rst
        time.sleep(3)   
        loop-=1
    return None
def get_idle_device():
    rst=__req('getDevices')
    for i in rst['devices']:
        if i['using']:
            continue
        return i['serial']
    return None
    
connect_to_stf('192.168.117.155:7100','8ad3024193ba44a1820afef3060df8934d964599b74049d4b11b9c3f9edb5457')
print get_user_name()
print getUserDevices()
print getIdleDevice()
print __req('getUserAccessTokens')

