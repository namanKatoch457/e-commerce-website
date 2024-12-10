from twilio.rest import Client

def send_sms(phone_number, message):
    account_sid = 'add you sid id'   
    auth_token = 'ad you token'
    twilio_phone_number = '+17756182911'

    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=phone_number
        )
        return {"success": True, "sid": message.sid}
    except Exception as e:
        return {"success": False, "error": str(e)}
