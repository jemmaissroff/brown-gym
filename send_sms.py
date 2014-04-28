from twilio.rest import TwilioRestClient
from account import account_sid
from account import auth_token
from account import from_number
# Your Account Sid and Auth Token from twilio.com/user/account
def send_treadmill_status(b, recipient):
	client = TwilioRestClient(account_sid, auth_token)
	if(b):
		body = "The treadmill is currently occupied."
	else:
		body = "No one is currently on the treadmill" 
	message = client.sms.messages.create(body = body,
	    to = recipient,    
	    from_ = from_number) 
	print message.sid

def send_invalid(recipient):
	client = TwilioRestClient(account_sid, auth_token)
	body = """I'm sorry, I don't understand. For the status of the treadmill please text me \"Treadmill\""""
	message = client.sms.messages.create(body = body,
	    to = recipient,    
	    from_ = from_number) 
	print message.sid