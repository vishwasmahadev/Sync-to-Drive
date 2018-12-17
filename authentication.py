#-------------------------------------------------------------------------------
# Name:        Authentication
# Purpose:
#
# Author:      vishwas.m
#
# Created:
# Copyright:   (c) vishwas.m
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from googleapiclient.discovery import build
from oauth2client import file, client, tools
from httplib2 import Http

#SCOPES = 'https://www.googleapis.com/auth/drive'

class Auth:
    #def __init__(self,SCOPES):
    def authenticate(self,SCOPES):
        #self.scopes=SCOPES
         #Authorization
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        http=creds.authorize(Http())
        return http

