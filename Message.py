import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(https://www.way2sms.com/api/v1/sendCampaign , 'P7LKYRZ07Z7ZW0R7Q5ZFGPEYZBYH1T03', 'XT70B2ENF9OYH8ZQ', 'stage', '9119675747', 'janusingh9889@gmail.com', 'how are you' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print response.text