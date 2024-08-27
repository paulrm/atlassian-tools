# atlassian-tools

to install requiered modules

`pip install python-dateutil humanize requests`


You’ll need to add the following secrets to your GitHub repository:

- JIRA_BASE_URL: Your JIRA instance URL.
- JIRA_USERNAME: Your JIRA username.
- JIRA_API_TOKEN: Your JIRA API token.
- JIRA_PROJECTS: Comma-separated list of JIRA project keys.
- EMAIL_USERNAME: The username for your email account.
- EMAIL_PASSWORD: The password or app-specific password for your email account.
- RECIPIENT_EMAIL: The email address to send the output to.
- SMTP server details:
    - server_address: Your SMTP server address.
    - server_port: Your SMTP server port (typically 587 for TLS).


# Error
```
Reporting-MTA: dns; merlot.neuroglia.com.ar
X-Postfix-Queue-ID: 1FD5CA006F
X-Postfix-Sender: rfc822; paul@enie.lat
Arrival-Date: Tue, 27 Aug 2024 08:04:04 +0000 (UTC)

Final-Recipient: rfc822; paul.messina@gmail.com
Original-Recipient: rfc822;paul.messina@gmail.com
Action: failed
Status: 5.7.26
Remote-MTA: dns; gmail-smtp-in.l.google.com
Diagnostic-Code: smtp; 550-5.7.26 Your email has been blocked because the
    sender is unauthenticated. 550-5.7.26 Gmail requires all senders to
    authenticate with either SPF or DKIM. 550-5.7.26  550-5.7.26
    Authentication results: 550-5.7.26  DKIM = did not pass 550-5.7.26  SPF
    [enie.lat] with ip: [23.29.118.199] = did not pass 550-5.7.26  550-5.7.26
    For instructions on setting up authentication, go to 550 5.7.26
    https://support.google.com/mail/answer/81126#authentication
    6a1803df08f44-6c162dd9ae1si128834716d6.407 - gsmtp
```