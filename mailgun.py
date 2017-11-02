import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox82b15a0e185b43d08896115aae76d63a.mailgun.org/messages",
        auth=("api", "key-09b37f8b0cc146089d2bcedf1e32b824"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox82b15a0e185b43d08896115aae76d63a.mailgun.org>",
              "to": "Jonathan <adamsjonathan1@gmail.com>",
              "subject": "Hello Jonathan",
              "text": "Congratulations Jonathan, you just sent an email with Mailgun!  You are truly awesome!"})

send_simple_message()
