# Host installation

	pip install Flask
	pip install python-crontab
	pip install twilio==6.1.0
	python client_script.py
	
	Note: it may be necessary to 'sudo apt install libssl-dev' if errors are thrown when trying to install twilio.
	
Host ip: 192.168.101.150:5000  --> This is the IP used when testing on the Virtual Network

# Infection

Host is a flask server that accepts incomming request. New email/phone numbers are sent links to the malicious website and prompted to install an Adobe Flash update. The client adds itself to the user's crontab and runs every hour. All emails and phone numbers found on the machine are sent to the host.

# DDOS Attack

Send a POST request to <hostip>:5000/ddos with the victim's ip and count of attacks. All clients who contact to the host after this POST request will send a GET request to the ip every 3 seconds <count> number of times. Send a new request to <hostip>:5000/ddos with ip = '' to end the ddos attack. This does not stop client's who are in the middle of their attack.

# Communication and Detailed Description

The client script uses grep to find emails and phone numbers on the client's computer. This could be extended to find other more malicious things like credit card numbers and social security numbers. Then the client will send lists of the email addresses and phone numbers that it found to the host. We originally wanted to encrypt this information but kept running into errors where the plaintext was too long. The text messages are sent with the Twilio API and the emails with SMTP. The host will send out emails and text messages using this information with a link to a website that look like a update for Adobe Flash. Tthe link is not actually included in this version because the website is only hosted locally on our virtual network (see website/README.md). If the user clicks the install button a compiled python script is downloaded so the user can not actually see the code. When the user runs the python file a setup install GUI runs that looks legitimate. While the loading bar is in progress a secret python file is made in documents that gets run every hour, this is the client script. Note: far more malicious behavior could be added to this script.
