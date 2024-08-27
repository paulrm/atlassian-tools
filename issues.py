import os
import requests
from requests.auth import HTTPBasicAuth
import json

# Load the JIRA API base URL and authentication credentials from environment variables
JIRA_BASE_URL = os.getenv('JIRA_BASE_URL')
JIRA_USERNAME = os.getenv('JIRA_USERNAME')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

# Load the list of project keys from the JIRA_PROJECTS environment variable
JIRA_PROJECTS = os.getenv('JIRA_PROJECTS', '').split(',')

def get_last_modified_tickets(project_key):
    # Define the JIRA API endpoint for searching issues
    search_url = f"{JIRA_BASE_URL}/rest/api/2/search"

    # JQL query to find the last modified issues in the given project
    jql_query = f"project = {project_key} ORDER BY updated DESC"

    # Define the search parameters, including the JQL query and fields to retrieve
    params = {
        'jql': jql_query,
        'fields': 'key,summary,updated',
        'maxResults': 10
    }

    # Make the API request
    response = requests.get(search_url, params=params, auth=HTTPBasicAuth(JIRA_USERNAME, JIRA_API_TOKEN))

    # Check if the request was successful
    if response.status_code == 200:
        issues = response.json().get('issues', [])
        return issues
    else:
        print(f"Failed to retrieve issues for project {project_key}. Status code: {response.status_code}")
        return []

def main():
    for project_key in JIRA_PROJECTS:
        print(f"\nLast modified tickets for project {project_key}:")

        # Retrieve the last modified tickets for the current project
        tickets = get_last_modified_tickets(project_key)

        # Print out the ticket details
        for ticket in tickets:
            key = ticket['key']
            summary = ticket['fields']['summary']
            updated = ticket['fields']['updated']
            print(f"{key}: {summary} (Last Updated: {updated})")

if __name__ == "__main__":
    main()
