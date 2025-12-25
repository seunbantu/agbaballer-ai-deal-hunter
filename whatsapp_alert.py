from twilio.rest import Client
from config import (
    TWILIO_SID,
    TWILIO_AUTH,
    WHATSAPP_FROM,
    WHATSAPP_TO
)

def send_alert(message):
    client = Client(TWILIO_SID, TWILIO_AUTH)

    client.messages.create(
        body=message,
        from_=WHATSAPP_FROM,
        to=WHATSAPP_TO
    )
