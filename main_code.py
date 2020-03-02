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
from pprint import pprint
import subprocess
import os

#------------------------------------------------------------------------------------



#--------------------[API Call AND JSON DUMP]---------------------------------------

#Chdir used as SSL wala Curl use karna hai
os.chdir(os.path.dirname(os.path.abspath(__file__)))

output_file='sardard.json'
symbol_nse='EIHOTEL'
nse_url= '"https://www.nseindia.com/api/quote-equity?symbol='+symbol_nse+'"'
# Headers me ched mad yehi time khata hai
nse_headers=' -H "authority: beta.nseindia.com" -H "cache-control: max-age=0" -H "dnt: 1" -H "upgrade-insecure-requests: 1" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36" -H "sec-fetch-user: ?1" -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "sec-fetch-site: none" -H "sec-fetch-mode: navigate" -H "accept-encoding: gzip, deflate, br" -H "accept-language: en-US,en;q=0.9,hi;q=0.8"'

cmd_nse= 'curl -k '+nse_url+nse_headers+' --compressed  -o '+output_file
# Without wait curl it reads buffer before the curl ka output aye
p1 = subprocess.Popen(cmd_nse, shell=True)
p1.wait()


f=open("sardard.json","r")
var=f.read()
response=json.loads(var)
print(response)

today_date = time.strftime("%m/%d/%Y")
#------------------------------------------------------------------------------------


logger.critical('DAEMON RUN COMPLETED SUCCESSFULLY')