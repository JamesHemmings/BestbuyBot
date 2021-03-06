from twilio.rest import Client
import os

def sms(message):
    # Your Account SID from twilio.com/console
    account_sid = "(your SID)"
    # Your Auth Token from twilio.com/console
    auth_token  = "(your auth token)"

    client = Client(account_sid, auth_token)

    message = client.messages.create(

        to=os.environ['PHONE_NUMBER'] , 
        from_="(your twilio phone number)",
        body = message
        )
