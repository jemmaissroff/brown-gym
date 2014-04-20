from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
def send_a_text(b):
	account_sid = ""
	auth_token  = ""
	client = TwilioRestClient(account_sid, auth_token)
	if(b):
		body = "The treadmill is currently occupied."
	else:
		body = "No one is currently on the treadmill" 
	message = client.sms.messages.create(body = body,
	    to="+",    
	    from_="+") 
	print message.sid