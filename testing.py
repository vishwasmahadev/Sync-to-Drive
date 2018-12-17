# -*- coding: utf-8 -*-

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from authentication import Auth
import logging

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

if __name__=='__main__':
    main()

