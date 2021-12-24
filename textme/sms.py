from twilio.rest import Client 
 
account_sid = 'AC0cd7e172372642a7081eed528e9a5dee' 
auth_token = '969a2c104981582ae21560f32d560705' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG80fa11b0192073cbbaa8946652f56261', 
                              body='hello how are you, OMG this works',      
                              to='+2348134870332' 
                          ) 
 
print(message.sid)