from twilio.rest import Client
import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

app= Flask(__name__)
app.config.from_object(__name__)

callers = {
    "+14039701456": "Suliat"
}

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    body = request.values.get('Body', None)
    args = body.split()

    import burn_notice
    arg_string = "burn_notice.py %s %s" % (args[0], args[1])
    os.system(arg_string)
    resp = MessagingResponse()
    resp.message("Alrighty! We'll remind you when to reapply your sunscreen!")
    return str(resp)


if __name__=="__main__":
    app.run(debug=True)
    