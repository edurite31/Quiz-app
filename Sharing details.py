import requests
import json

# Function to share product details on Facebook
def share_on_facebook(product_details, access_token):
    url = f"https://graph.facebook.com/v12.0/me/feed"
    payload = {
        'message': product_details,
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    return response.json()

# Function to share product details on Twitter
def share_on_twitter(product_details, bearer_token):
    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": product_details
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Function to share product details on LinkedIn
def share_on_linkedin(product_details, access_token):
    url = "https://api.linkedin.com/v2/shares"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": {
            "contentEntities": [],
            "title": product_details
        },
        "distribution": {
            "linkedInDistributionTarget": {}
        },
        "owner": "urn:li:person:YOUR_LINKEDIN_USER_ID",
        "subject": "New Product Launch",
        "text": {
            "text": product_details
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Main function to share product details
def share_product_details(product_details):
    facebook_access_token = "YOUR_FACEBOOK_ACCESS_TOKEN"
    twitter_bearer_token = "YOUR_TWITTER_BEARER_TOKEN"
    linkedin_access_token = "YOUR_LINKEDIN_ACCESS_TOKEN"

    facebook_response = share_on_facebook(product_details, facebook_access_token)
    twitter_response = share_on_twitter(product_details, twitter_bearer_token)
    linkedin_response = share_on_linkedin(product_details, linkedin_access_token)

    print("Facebook Response:", facebook_response)
    print("Twitter Response:", twitter_response)
    print("LinkedIn Response:", linkedin_response)

# Example product details
product_details = "Check out our new product: Amazing Widget 3000! Available now at www.example.com"

# Share product details on social media
share_product_details(product_details)
