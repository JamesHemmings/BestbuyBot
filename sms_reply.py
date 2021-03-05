    
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask
app = Flask(__name__)

@app.route("/sms", methods =['POST'])
def sms_reply():
    number = request.form['From']
    m_b = request.form['Body']
    response_message='unknown response, type "commands" for a list of known words'
    resp = MessagingResponse()
    print(m_b)
    if m_b=='hello' or m_b== 'Hello':
        response_message='Hi,how are you?'
         
    elif m_b=='COMMANDS' or m_b== 'commands' or m_b== 'Commands':
        response_message='hello,.....'

    resp.message(response_message)
    #add new endpoint has new message come in, add variable for text message recieved and time 
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

