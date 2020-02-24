#####################################################################################
#                                                                                   #
# ▒█▀▀▀█ ▒█░░▒█ ▒█▄░▒█ ▒█▀▀█ 　 ▒█▀▀▄ ░█▀▀█ ▒█▀▀▀ ▒█▀▄▀█ ▒█▀▀▀█ ▒█▄░▒█              #
# ░▀▀▀▄▄ ▒█▄▄▄█ ▒█▒█▒█ ▒█░░░ 　 ▒█░▒█ ▒█▄▄█ ▒█▀▀▀ ▒█▒█▒█ ▒█░░▒█ ▒█▒█▒█              #
# ▒█▄▄▄█ ░░▒█░░ ▒█░░▀█ ▒█▄▄█ 　 ▒█▄▄▀ ▒█░▒█ ▒█▄▄▄ ▒█░░▒█ ▒█▄▄▄█ ▒█░░▀█              #
#                                                                                   #
#                                                                                   #
#                                                                                   #
#   MariaDB --> JSON --> Connector --> PYDOBC(.mdb) --> TrueCAFE                    #
#                                  --> MS SQL Serv  --> ZkAccess                    #
#                                                                                   #
#                                                                                   #
#####################################################################################
import datetime,time
import urllib.request as urllib
import hashlib 

#---------------------[APP LOGGING]--------------------------------------------------
import logging.config
from datetime import datetime

logging.config.fileConfig('logger.conf')
logger = logging.getLogger('MainLogger')

fh = logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now()))
formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(lineno)04d | %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)
logger.critical("THE DAEMON RUN INITIAED")

#------------------------------------------------------------------------------------

#--------------------[FOR API]-------------------------------------------------------
import json,ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
api_key='5062acabf92c4007835e04cc8734a20c'
#------------------------------------------------------------------------------------




#--------------------[API Call AND JSON DUMP]---------------------------------------
url='https://monuabhaysv-eval-prod.apigee.net/svabhay2' 
logger.info('URL Generated :'+url)
a=urllib.urlopen(url,context=ctx).read().decode()
response=json.loads(a)

today_date = time.strftime("%m/%d/%Y")
#------------------------------------------------------------------------------------


logger.critical('DAEMON RUN COMPLETED SUCCESSFULLY')