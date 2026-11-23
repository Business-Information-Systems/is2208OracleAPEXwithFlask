from flask import Flask, render_template
app = Flask(__name__)

import requests

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml",
    "accept-language": "en-GB,en-US",
    "sec-fetch-dest": "document",
    "user-agent": (
        "Mozilla/5.0 (iPad; CPU OS 18_5 like Mac OS X) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Version/18.5 Mobile/15E148 Safari/604.1"
    ),
}

base_url = "https://oracleapex.com/ords/is22082/"

client_id = "7cyvcpfdn8tQkrezKYQLEA.."
client_secret = "6jBgOg2iHHaPJQg3rvPgsg.."

def get_data_from_apex():
    response = requests.post(
        base_url + "oauth/token",
        auth=(client_id, client_secret),
        data={"grant_type": "client_credentials"},
        headers=headers,
        timeout=(10, 20),
    )

    if response.status_code != 200:
        return(response.status_code)
    else:
        token = response.json()["access_token"]

        response = requests.get(
            base_url + "students/",
            headers={
                **headers,
                "Authorization": f"Bearer {token}",
            },
            timeout=(10, 20),
        )
        data = response.json()["items"]
        items = []
        for item in data:
            items.append([item["id"], item["name"]])
        return items

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html",items=get_data_from_apex())

if __name__ == '__main__':
    app.run()
