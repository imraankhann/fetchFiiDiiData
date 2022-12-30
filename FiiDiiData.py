from pytz import timezone
import datetime
import telegram
import numpy as np
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account
from time import sleep
import requests


format = "%d-%m-%Y"
dtToday = datetime.datetime.today()
dtFrmtToday = dtToday.strftime(format)
dtTodayStr = str(dtFrmtToday.replace('-', ''))
dtYesterday = dtToday - datetime.timedelta(days=1)
dtFrmtYest = dtYesterday.strftime(format)
dtYesterStr = str(dtFrmtYest.replace('-', ''))
dtYesterLst = [[dtYesterStr]]
dtTodayLst = [[dtTodayStr]]

print("Date Today : "+dtTodayStr + "\t"+"Date Yesterday : "+dtYesterStr)


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# SPREAD SHEET ID

SAMPLE_SHEET_ID = '19hThI-kRbTcKaUI2RqZzHlmuworlME6i9v-jUSK_IFw'
service = build('sheets', 'v4', credentials=creds)

# Call the sheet api
sheet = service.spreadsheets()

# request = sheet.values().update(spreadsheetId=SAMPLE_SHEET_ID, range="Yday!B1",
#                                 valueInputOption="USER_ENTERED", body={"values": dtYesterLst}).execute()
# request = sheet.values().update(spreadsheetId=SAMPLE_SHEET_ID, range="Today!B1",
#                                 valueInputOption="USER_ENTERED", body={"values": dtTodayLst}).execute()
# print("Waiting for 15 seconds started....!")
# sleep(15)
# print("Wait for 15 seconds completed..!")
result = sheet.values().get(spreadsheetId=SAMPLE_SHEET_ID,
                            range="MasterComparison!A11:D16").execute()
values = result.get('values', [])
listToStr = ''.join(map(str, values))
nextLineResult = listToStr.replace(
    "[", "]\n").replace(']', ' ').replace("'", "")
notifyTelegram = "Index Options FII, DII and PRO data"
print("Results : "+"==================\n"+notifyTelegram +
      "\n"+"====================\n"+nextLineResult)
t_url2 = "https://api.telegram.org/bot5771720913:AAH0A70f0BPtPjrOCTrhAb9LR7IGFBVt-oM/sendMessage?chat_id=-703180529&text=" + str(dtToday) + \
    "\n"+"========================\n"+notifyTelegram + \
    "\n"+"========================\n"+nextLineResult
requests.post(t_url2)


# 27122022#
