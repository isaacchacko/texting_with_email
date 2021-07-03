# TEXTING WITH EMAIL ADDRESSES

this repository stores code that can text someone through their service provider's email address. To text someone, input their phone number, and what service provider they use (only accepts verizon, t-mobile, at&t, and sprint), and the message you want to send.

### Required Libraries:

- os

- json

- smtplib

### Saving Contacts:

The code allows for you to save your contacts onto a "contacts.json" file, however I'm not gonna upload mine in fear of doxxing. The format is as below:

```json
{"contact_name": {"num": 1234567890, "provider": "t-mobile"}}
```
