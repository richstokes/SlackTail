# Slack-Tail
Tail a log file (or any other input) to a Slack channel
<br><br>
This is designed for anyone wishing to share a log file or any other text-input in real time to a Slack channel. Possible uses include debugging a system or application with a team in real time.<br><br>To get working, you will need to create an Incoming Webhook URL for your Slack team (https://api.slack.com/incoming-webhooks). You can then enter this by editing the lines in slackTail.py<br><br><br>
*Start the server with ./slackTail.py *<br><br>

Then pipe some log files at it. I suggest using netcat (nc), but any raw UDP client should work fine. Example:
<br><br>
tail -F /var/log/apache2/error.log | nc -u 127.0.0.1 9999
<br><br>
