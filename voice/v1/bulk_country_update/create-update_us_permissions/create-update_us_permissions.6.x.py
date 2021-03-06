# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

bulk_country_update = client.voice \
    .voice_permissions \
    .bulk_country_updates \
    .create(
         update_request="[{'iso_code': 'US', 'low_risk_numbers_enabled': 'true', 'high_risk_special_numbers_enabled': 'true', 'high_risk_tollfraud_numbers_enabled': 'true'}]"
     )

print(bulk_country_update.update_count)
