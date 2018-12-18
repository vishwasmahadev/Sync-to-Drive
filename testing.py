# -*- coding: utf-8 -*-

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from authentication import Auth
import logging
import zipfile
import os

def main():

    logging.basicConfig(filename='runner.log', filemode='a+',format='%(levelname)s -> %(asctime)s: %(message)s', level=logging.DEBUG)
    auth=Auth().authenticate('https://www.googleapis.com/auth/drive')

    try:
        service=build('drive', 'v3', auth)
        res = service.files().create(media_body=r'C:\Users\vishwas.m\Desktop\ESI.xml', body={'name': 'esi'}).execute()
        responseFileName=res.get('name')
        logging.info(responseFileName)
    finally:
      print("In finally code")

##    file_path=[]
##    for root,folder,file in os.walk(r"C:\Users\vishwas.m\Desktop\API Gateway\Sample Runbook"):
##        for files in file:
##                file_path.append(os.path.join(root,files))
##    print(file_path)
##    with zipfile.ZipFile(r'C:\Users\vishwas.m\Desktop\API Gateway\Sample Runbook\zipped.zip','w') as zip:
##      for file in file_path:
##          zip.write(file)

if __name__=='__main__':
    main()



