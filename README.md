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