from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER


def notifyOfTag(number, content, image=None):
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # try:
    if image:
        client.messages.create(
            to=number, 
            _from=TWILIO_NUMBER, 
            body=content,
            media_url=image
        )
    else:
        client.messages.create(
            to=number, 
            _from=TWILIO_NUMBER, 
            body=content,
        )
    # except TwilioRestException:
    #    print("Message not sent!")