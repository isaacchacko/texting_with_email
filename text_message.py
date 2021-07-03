import os
import json
import smtplib

class ServiceNotAvaliableError(Exception):
	pass


class Contacts:
	def __init__(self):
		self.filename = 'contacts.json'
		if os.path.isfile(self.filename):
			self.contacts = self.load()
		else:
			self.contacts = {}

	def load(self):
		with open(self.filename, 'r') as f:
			return json.loads(f.read())
	
	def save(self):
		with open(self.filename, 'w') as f:
			f.write(json.dumps(self.contacts))

class Phone(Contacts):
	def __init__(self, email_address, email_pass, emailing_service):

		self.possible_services = ['gmail']
		self.servers = {'gmail': 'smtp.gmail.com'}
		self.ssl_ports = {'gmail': 465}
		self.providers = {'at&t': '@mms.att.net',
						  't-mobile': '@tmomail.net',
						  'verizon': '@vtext.com',
						  'sprint': '@page.nextel.com'}

		self.email_address, self.email_pass, self.emailing_service = email_address, email_pass, emailing_service

		if self.emailing_service in self.possible_services:
			self.port = self.ssl_ports[self.emailing_service]
			self.server = self.servers[self.emailing_service]
		else:
			raise ServiceNotAvaliableError('"{}" is not a working service at this time.'.format(self.emailing_service))


		Contacts.__init__(self)
	def text(self, to, message, service_provider = None):
		with smtplib.SMTP_SSL(self.server, self.port) as smtp:
			smtp.login(self.email_address, self.email_pass)

			if type(to) == str:
				service_provider = self.contacts[to]['provider']
				to = self.contacts[to]['num']

			receiver_email = str(to) + self.providers[service_provider]
			message = ("From: %s\r\n" % self.email_address + "To: %s\r\n" % str(to) + "Subject: %s\r\n" % '' + "\r\n" + message)

			smtp.sendmail(self.email_address, receiver_email, message)

			# check if number in contacts
			if to not in self.contacts.values():
				self.contacts[str(to)] = {'num': to, 'provider': service_provider}


if __name__ == '__main__':
	EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
	EMAIL_PASS = os.getenv('EMAIL_PASS')
	iphone = Phone(EMAIL_ADDRESS, EMAIL_PASS, 'gmail')
	iphone.text('alex', """boping says you SMELL but again""")
	iphone.save()