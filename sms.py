import os
from twilio.rest import Client

account_sid = 'AC20ae234405b304d03111b5ae30439'
auth_token = 'ae2682f54756a4dfdsfasd5f48e255aa'
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="test",
                     from_='Twilio_num',
                     to='Personal_num'
                 )
print(message.sid)
