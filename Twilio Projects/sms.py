from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "A*******************************"
# Your Auth Token from twilio.com/console
auth_token  = "********************************"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+1525562652", 
    from_="+1515325666",
    body="Hello from Python!")

print(message.sid)
