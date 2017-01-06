#!/usr/bin/python3
#June 2016
#This python script creates a simple UDP server which will relay all incoming text to a Slack channel
import socketserver
import requests
import json

#Create a new Incoming JSON Webhook in your Slack admin control panel, and paste the link below
webhook_url = 'https://hooks.slack.com/services/ABCDEFG/ABCDEFG/ABCDEFGABCDEFG'

#Define IP and port to listen on (UDP)
HOST, PORT = "127.0.0.1", 9999

#Custom variables
name = "Johnny 5"

#Feel free to change the channel, username, emoji here:
def slackpost(msg):
	slack_data = {'channel': '#general', 'username': name, 'text': msg, 'icon_emoji': ':ghost:'}
	response = requests.post(
    	webhook_url, data=json.dumps(slack_data),
    	headers={'Content-Type': 'application/json'}
)

#End of stuff you need to configure :-)



class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} sent:".format(self.client_address[0]))
        print(data)
        dataclean = str(data, errors='ignore')
        slackpost(dataclean)
#Uncomment line below to send message back to client for debugging:
#        socket.sendto((data), self.client_address)

if __name__ == "__main__":
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
