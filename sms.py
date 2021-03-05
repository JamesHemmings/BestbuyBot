from twilio.rest import Client
import os

def sms(message):
    # Your Account SID from twilio.com/console
    account_sid = "ACd147f4df6e07dff7a845e8613b4aec65"
    # Your Auth Token from twilio.com/console
    auth_token  = "6c70481a99e491f5a12af3caeae47c40"

    client = Client(account_sid, auth_token)

    message = client.messages.create(

        to=os.environ['PHONE_NUMBER'] , 
        from_="+14696544211",
        body = message
        )
