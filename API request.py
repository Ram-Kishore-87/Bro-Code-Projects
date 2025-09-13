import requests
import random
import json




def rizz(name):
    base_url = "https://o1swy96l80.execute-api.ap-south-1.amazonaws.com/api/random"
    response=requests.get(base_url)

    if response.status_code == 200:
        data=response.json()
        body=json.loads(data["body"])
        pickup = body["pickupLine"]["text"]
        return f"Hey {name},{pickup}🤞"

    else:

        fallback=[
            "Are you a meth lab? Because you’ve got me cooking up some serious feelings",
            "Is your name Jesse? Because you’re making my heart go yo, Mr. White!",
            "Like Saul Goodman says: Better call me if you’re looking for fun!"
        ]
        return f" Hey {name}, {random.choice(fallback)}"

if __name__ == "__main__":
    user = input(" YO What\'s  your name? ")
    print(rizz(user))
