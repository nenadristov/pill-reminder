import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC07804832895d05568ef8134b1d51a263'
auth_token = 'd95b620a88bd001126e27dc06eabc411'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="SMS poraka test",
                     from_='+16789819653',
                     to='+38978980433'
                 )

print(message.sid)