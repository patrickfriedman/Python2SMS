import os
from twilio.rest import Client

account_sid = 'AC20aef97ee2405b304d03111b5ae30439'
auth_token = 'ae2682f547d1235d992c4bd32917f5aa'
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="test",
                     from_='+19725034157',
                     to='+12144713159'
                 )
print(message.sid)