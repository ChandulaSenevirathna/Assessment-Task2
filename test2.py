import requests

#Credentials to the endpoint
client_id = 'a6fc6129-e8f8-4a87-a35c-6fe2a5b25c38'
client_secret = 'd6f433ee-33fe-47cd-8804-fd5a586b5900'
refresh_token = '3e242fdc-8f23-432b-97bb-692125049a3a'
access_token_url = 'https://api.hubapi.com/oauth/v1/token'
contacts_endpoint = 'https://api.hubapi.com/crm/v3/objects/contacts' #API endpoint

#Obtain a new access token using the refresh token
def get_access_token():
    data = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
    }
    response = requests.post(access_token_url, data=data)
    response_data = response.json()
    if response.status_code == 200:
        return response_data['access_token']
    else:
        raise Exception(f"Failed to obtain access token: {response_data}")

# Use the access token to make a GET request to the contacts endpoint
def get_contacts(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    response = requests.get(contacts_endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve contacts: {response.json()}")

# Obtain the access token
access_token = get_access_token()
# print("Access Token:", access_token)

# Fetch contacts using the access token
contacts = get_contacts(access_token)
# print("Contacts:", contacts)

# Print the IDs of the contacts
for contact in contacts['results']:
    # print(contact)
    print(f"Contact ID: {contact['id']}")
    print(f"First Name: {contact['properties']['firstname']}")
    print(f"Last Name: {contact['properties']['lastname']}")
    print(f"Contact Email: {contact['properties']['email']}")
    print("\n")
    